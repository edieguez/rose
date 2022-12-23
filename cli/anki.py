import genanki
from jinja2 import Environment, FileSystemLoader

deck = genanki.Deck(1802257999, 'Rose dictionary')


def add_note(word, definitions):
    note = genanki.Note(
        genanki.BASIC_TYPE_IN_THE_ANSWER_MODEL,
        fields=[_parse_definitions(definitions), word]
    )

    deck.add_note(note)


def _parse_definitions(definitions):
    env = Environment(loader=FileSystemLoader('resources/templates'))
    template = env.get_template('word_definition.html')

    parsed_definitions = []

    for definitions in definitions.values():
        for definition in definitions:
            print(definition.description)
            parsed_definitions.append(definition)

    context = {
        'definitions': parsed_definitions
    }

    return template.render(context)


def export_deck():
    package = genanki.Package(deck)
    package.media_files = []
    package.write_to_file('rose.apkg')
