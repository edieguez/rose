#! /usr/bin/env python
from dictionary import free_dictionary
from database import dao

print('Rose project')

dao.create_initial_database()
result = free_dictionary.query('test')

dao.insert_word(result)

print(f'TEXT: {result.text}')
