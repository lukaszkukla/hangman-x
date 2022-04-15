import requests
from src.lang import language

APIURL = 'https://random-word-api.herokuapp.com'

def get_word(lang='en'):
    '''
    Gets the word from the API
    '''
    res = requests.get(f'{APIURL}/word?lang={lang}')
    try:
        res.raise_for_status()
        return res.json()[0]
    except requests.exceptions.InvalidURL as erru:
        print(f'invalid url {erru}')
    except requests.exceptions.HTTPError as errh:
        print(f'invalid http response {errh}')
    except requests.exceptions.ConnectionError as errc:
        print(f'connection error {errc}')
    except requests.exceptions.Timeout as errt:
        print(f'connection timeout error {errt}')
    except requests.exceptions.RequestException as err:
        print(f'unknown exception error {err}')
