import requests
from model import entities

API_URL = 'https://api.dictionaryapi.dev/api/v2/entries/en'


def query(word):
    response = requests.get(f'{API_URL}/{word}')

    if response.status_code == 200:
        return json_to_entity(response.json())


def json_to_entity(json):
    return entities.Word(json[0].get('word'))
