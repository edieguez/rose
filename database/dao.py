import os
import sqlite3

from dictionary import unsplash
from model import entities


def create_initial_database():
    if not os.path.exists('database.sqlite'):
        conn, cursor = _get_conn()

        with open('resources/schema.sql', 'r') as f:
            cursor.executescript(f.read())

        conn.commit()


def insert_word(word):
    word_image_url = unsplash.get_image_url(word.text)
    conn, cursor = _get_conn()

    with conn:
        cursor.execute('INSERT INTO words (text, image_url) VALUES (?, ?)', (word.text, word_image_url))


def get_word_by_text(text):
    raw_word = _get_raw_word_by_text(text)

    return entities.Word(raw_word[0], raw_word[1], raw_word[2]) if raw_word else None


def get_all_words():
    conn, cursor = _get_conn()

    with conn:
        db_words = conn.execute('SELECT id, text, image_url FROM words')

        return [entities.Word(word[0], word[1], word[2]) for word in db_words.fetchall()]


def get_definitions_by_word_id(word_id):
    conn, cursor = _get_conn()

    with conn:
        db_definitions = conn.execute('SELECT part_of_speech, description, example FROM definitions WHERE words_id = ?',
                                      (word_id,))

        definitions = db_definitions.fetchall()
        segregated_definitions = {}

        for definition in definitions:
            if definition[0] not in segregated_definitions:
                segregated_definitions[definition[0]] = []

            segregated_definitions[definition[0]].append(
                entities.Definition(definition[1], definition[0], definition[2]))

        return segregated_definitions


def insert_definitions(word, definitions):
    conn, cursor = _get_conn()

    with conn:
        for partOfTheSpeech, meanings in definitions.items():
            for meaning in meanings:
                cursor.execute(
                    'INSERT INTO definitions(words_id, part_of_speech, description, example) VALUES(?, ?, ?, ?)', (
                        word.id, partOfTheSpeech, meaning.description, meaning.example
                    ))


def _get_raw_word_by_text(text):
    conn, cursor = _get_conn()

    with conn:
        db_word = conn.execute('SELECT id, text, image_url FROM words WHERE text = ?', (text,))

        return db_word.fetchone() if db_word else None


def _get_conn(database='database.sqlite'):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    return conn, cursor
