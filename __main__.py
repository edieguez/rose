#! /usr/bin/env python
from database import dao
from dictionary import free_dictionary
from cli import anki

print('Rose project')

dao.create_initial_database()
term = 'awe'

result = free_dictionary.query(term)
word = dao.get_word_by_text(result.text)

if not word:
    print(f'Word {term} not found in database')

    dao.insert_word(result)
    word = dao.get_word_by_text(result.text)

    dao.insert_definitions(word, result.definitions)
    anki.add_note(word.text, result.definitions)

anki.export_deck()
