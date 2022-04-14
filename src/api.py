import requests

APIURL = 'https://random-word-api.herokuapp.com'

def get_word():  
    '''
    Gets the word from the API
    '''  
    res = requests.get(f'{APIURL}/word')
    try:        
        res.raise_for_status()
        return res.json()[0]
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

def call_get_word():
    return get_word()
