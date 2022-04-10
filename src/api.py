import requests

APIURL = requests.get('https://random-word-api.herokuapp.com/word?number=1&swear=0', timeout=3)

# exception handling code borrowed from
# https://www.nylas.com/blog/use-python-requests-module-rest-apis/

def get_word(url):
    try:        
        url.raise_for_status()
        return url.json()
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

def call_get_word():
    word = get_word(APIURL)[0]
    return word
