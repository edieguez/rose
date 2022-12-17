import sqlite3
import os


def create_initial_database():
    if not os.path.exists('database.sqlite'):
        cursor = _get_cursor()

        with open('resources/schema.sql', 'r') as f:
            cursor.executescript(f.read())


def _get_cursor(database='database.sqlite'):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    return cursor
