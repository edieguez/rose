class Word:
    def __init__(self, id_=None, text=None, image_url=None, definitions=None):
        self.id = id_
        self.text = text
        self.image_url = image_url
        self.definitions = definitions

    def __repr__(self):
        return f'Word(id={self.id}, text={self.text}, definitions={self.definitions})'


class Definition:
    def __init__(self, description, part_of_speech=None, example=None):
        self.part_of_speech = part_of_speech
        self.description = description
        self.example = example

    def __repr__(self):
        return f'Definition(description={self.description}, example={self.example})'
