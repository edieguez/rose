#! /usr/bin/env python
import sys

from cli import anki
from database import dao
from dictionary import free_dictionary


def parse_arguments():
    if len(sys.argv) <= 1:
        print('No arguments provided')
        sys.exit(1)


if __name__ == '__main__':
    parse_arguments()

    dao.create_initial_database()
    term = sys.argv[1]

    result = free_dictionary.query(term)

    if not result:
        print(f'{term} definition not found')
        sys.exit(2)

    word = dao.get_word_by_text(result.text)

    if not word:
        print(f'Word {term} not found in database')

        dao.insert_word(result)
        word = dao.get_word_by_text(result.text)

        dao.insert_definitions(word, result.definitions)
        anki.add_note(word.text, result.definitions)
    else:
        print(f'Word {term} found in database. Nothing to do')

    anki.export_deck()
