import sqlite3
import os

from model import entities


def create_initial_database():
    if not os.path.exists('database.sqlite'):
        conn, cursor = _get_conn()

        with open('resources/schema.sql', 'r') as f:
            cursor.executescript(f.read())

        conn.commit()


def insert_word(word):
    conn, cursor = _get_conn()

    with conn:
        cursor.execute('INSERT INTO words (text) VALUES (?)', (word.text,))


def get_word_by_text(text):
    raw_word = _get_raw_word_by_text(text)

    return entities.Word(raw_word[0], raw_word[1]) if raw_word else None


def get_all_words():
    conn, cursor = _get_conn()

    with conn:
        db_words = conn.execute('SELECT id, text FROM words')

        return [entities.Word(word[0], word[1]) for word in db_words.fetchall()]


def get_definitions_by_word_id(word_id):
    conn, cursor = _get_conn()

    with conn:
        db_definitions = conn.execute('SELECT description, example FROM definitions WHERE words_id = ?', (word_id,))

        return [entities.Definition(definition[0], definition[1]) for definition in db_definitions.fetchall()]


def insert_definitions(word, definitions):
    conn, cursor = _get_conn()

    with conn:
        for partOfTheSpeech, meanings in definitions.items():
            for meaning in meanings:
                cursor.execute(
                    'INSERT INTO definitions(words_id, description, example) VALUES(?, ?, ?)', (
                        word.id, meaning.description, meaning.example
                    ))


def _get_raw_word_by_text(text):
    conn, cursor = _get_conn()

    with conn:
        db_word = conn.execute('SELECT id, text FROM words WHERE text = ?', (text,))

        return db_word.fetchone() if db_word else None


def _get_conn(database='database.sqlite'):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    return conn, cursor
