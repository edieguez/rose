import os
import sqlite3

import cli
from dictionary import unsplash
from model import entities


def create_initial_database():
    if not os.path.exists(os.path.join(cli.base_dir, 'rose.sqlite3')):
        conn, cursor = _get_conn()

        with open(os.path.join(cli.inner_base_dir, 'resources', 'schema.sql'), 'r') as f:
            cursor.executescript(f.read())

        conn.commit()


def insert_word(word):
    word_image_url = unsplash.get_image_url(word.text)
    conn, cursor = _get_conn()

    with conn:
        cursor.execute('INSERT INTO words (text, phonetic, image_url, audio_url) VALUES (?, ?, ?, ?)',
                       (word.text, word.phonetic, word_image_url, word.audio_url))


def get_word_by_text(text):
    raw_word = _get_raw_word_by_text(text)

    return entities.Word(raw_word[0], raw_word[1], raw_word[2], raw_word[3]) if raw_word else None


def get_all_words():
    conn, cursor = _get_conn()

    with conn:
        db_words = conn.execute('SELECT id, text, phonetic, image_url, audio_url FROM words')

        return [entities.Word(word[0], word[1], word[2], word[3], word[4]) for word in db_words.fetchall()]


def get_definitions_by_word_id(word_id):
    conn, cursor = _get_conn()

    with conn:
        db_definitions = conn.execute('SELECT part_of_speech, description, example FROM definitions WHERE words_id = ?',
                                      (word_id,))
        return [entities.Definition(definition[1], definition[0], definition[2]) for definition in
                db_definitions.fetchall()]


def insert_definitions(word, definitions):
    conn, cursor = _get_conn()

    with conn:
        for definition in definitions:
            cursor.execute(
                'INSERT INTO definitions (words_id, part_of_speech, description, example) VALUES (?, ?, ?, ?)',
                (word.id, definition.part_of_speech, definition.description, definition.example))


def _get_raw_word_by_text(text):
    conn, cursor = _get_conn()

    with conn:
        db_word = conn.execute('SELECT id, text, phonetic, image_url FROM words WHERE text = ?', (text,))

        return db_word.fetchone() if db_word else None


def _get_conn():
    database_file = os.path.join(cli.base_dir, 'rose.sqlite3')

    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    return conn, cursor
