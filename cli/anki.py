import genanki

deck = genanki.Deck(1802257999, 'Rose dictionary')


def add_note(word, definitions):
    note = genanki.Note(
        genanki.BASIC_TYPE_IN_THE_ANSWER_MODEL,
        fields=[definitions, word]
    )

    deck.add_note(note)


def export_deck():
    package = genanki.Package(deck)
    package.media_files = []
    package.write_to_file('rose.apkg')
