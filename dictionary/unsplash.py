import os
import requests

UNSPLASH_API_KEY = os.environ.get('UNSPLASH_API_KEY')


def check_api_key():
    if not UNSPLASH_API_KEY:
        print('UNSPLASH_API_KEY environment variable not set')
        return False

    return True


def get_image_url(query):
    if not check_api_key():
        return

    response = requests.get(f'https://api.unsplash.com/search/photos?query={query}&client_id={UNSPLASH_API_KEY}')

    if response.status_code == 200:
        json = response.json()['results']

        if json:
            return json[0]['urls']['regular']
