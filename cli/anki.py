import genanki
from jinja2 import Environment, FileSystemLoader

from database import dao
from model import entities


def add_note(deck, word, definitions):
    note = genanki.Note(
        genanki.BASIC_TYPE_IN_THE_ANSWER_MODEL,
        fields=[_parse_definitions(definitions), word]
    )

    deck.add_note(note)


def _parse_definitions(definitions):
    env = Environment(loader=FileSystemLoader('resources/templates'))
    template = env.get_template('word_definition.html')

    parsed_definitions = {}

    for part_of_speech, meanings in definitions.items():
        parsed_definitions[part_of_speech] = [entities.Definition(part_of_speech, meaning.description, meaning.example)
                                              for meaning in meanings]

    context = {
        'definitions': parsed_definitions
    }

    return template.render(context)


def export_deck(deck_name):
    deck = genanki.Deck(1802257999, 'Rose dictionary')
    filename = f'{deck_name}.apkg'
    print(f'Exporting to {filename}')

    for word in dao.get_all_words():
        definitions = dao.get_definitions_by_word_id(word.id)
        add_note(deck, word.text, definitions)

        print(f'Found {len(definitions)} definitions for {word.text}')

    package = genanki.Package(deck)
    package.media_files = []
    package.write_to_file(filename)
