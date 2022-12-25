class Word:
    def __init__(self, id, text, definitions=None):
        self.id = id
        self.text = text
        self.definitions = definitions

    def __repr__(self):
        return f'Word(id={self.id}, text={self.text}, definitions={self.definitions})'


class Definition:
    def __init__(self, part_of_speech, description, example):
        self.part_of_speech = part_of_speech
        self.description = description
        self.example = example

    def __repr__(self):
        return f'Definition(description={self.description}, example={self.example})'
