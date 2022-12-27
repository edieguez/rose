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
    parser.add_argument('-e', '--export', type=str, nargs='?', const='rose_dict', metavar='filename',
                        help='Anki deck name')
    parser.add_argument('words', nargs='*', help='Words to be added to the dictionary')

    return parser.parse_args()


def save_word_definitions(words: list):
    for word in words:
        query_word_definition(word)


def query_word_definition(term: str):
    api_word, api_definitions = free_dictionary.query(term)

    if not api_word:
        print(f'{term} definition not found')
        return

    db_word = dao.get_word_by_text(api_word.text)

    if not db_word:
        print(f'Word {term} not found in database')

        dao.insert_word(api_word)
        db_word = dao.get_word_by_text(api_word.text)

        dao.insert_definitions(db_word, api_definitions)

        _print_definitions(api_definitions)
    else:
        print(f'Word {term} found in database. Nothing to do')


def _print_definitions(definitions):
    for definition in definitions:
        print(f'[{definition.part_of_speech}] {definition.description} - ({definition.example})')


if __name__ == '__main__':
    args = parse_arguments()
    dao.create_initial_database()

    if args.export:
        anki.export_deck(args.export)
    else:
        save_word_definitions(args.words)
