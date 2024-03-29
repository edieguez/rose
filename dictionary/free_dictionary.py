import requests

from model import entities

API_URL = 'https://api.dictionaryapi.dev/api/v2/entries/en'


def query(word):
    response = requests.get(f'{API_URL}/{word}')

    if response.status_code == 200:
        return _json_to_entity(response.json())

    return None, None


def _json_to_entity(json):
    definitions = []
    phonetic = None
    audio_url = None

    for word in json:
        for phonetic in word['phonetics']:
            if phonetic['audio']:
                audio_url = phonetic['audio']
                break

        phonetic = word.get('phonetic', None)

        for meaning in word['meanings']:
            for definition in meaning['definitions']:
                definition = entities.Definition(
                    definition.get('definition'),
                    meaning['partOfSpeech'],
                    definition.get('example', None)
                )

                definitions.append(definition)

        break

    return entities.Word(text=json[0].get('word'), phonetic=phonetic, audio_url=audio_url), definitions
