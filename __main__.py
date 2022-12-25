#! /usr/bin/env python
import argparse
import sys

from cli import anki
from database import dao
from dictionary import free_dictionary


def parse_arguments():
    if len(sys.argv) <= 1:
        print('No arguments provided')
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--export', type=str, nargs='?', const='rose_dict', metavar='filename', help='Anki deck name')
    parser.add_argument('words', nargs='*', help='Words to be added to the dictionary')

    return parser.parse_args()


def save_word_definitions(words: list):
    for word in words:
        query_word_definition(word)


def query_word_definition(term: str):
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


if __name__ == '__main__':
    args = parse_arguments()
    dao.create_initial_database()

    if args.export:
        anki.export_deck(args.export)
    else:
        save_word_definitions(args.words)
