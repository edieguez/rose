import sqlite3
import os


def create_initial_database():
    if not os.path.exists('database.sqlite'):
        conn, cursor = _get_conn()

        with open('resources/schema.sql', 'r') as f:
            cursor.executescript(f.read())

        conn.commit()


def insert_word(word):
    conn, cursor = _get_conn()

    with conn:
        db_word = get_word_by_text(word.text)

        if not db_word:
            cursor.execute('INSERT INTO words (text) VALUES (?)', (word.text,))


def get_word_by_text(text):
    conn, cursor = _get_conn()

    with conn:
        db_word = conn.execute('SELECT id FROM words WHERE text = ?', (text,))

        return db_word.fetchone() if db_word else None


def _get_conn(database='database.sqlite'):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    return conn, cursor
