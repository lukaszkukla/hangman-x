import requests

# APIURL = requests.get('https://random-word-api.herokuapp.com/word', timeout=3)



# original link - stopped working
# https://random-word-api.herokuapp.com/word?number=1&swear=0

# exception handling code borrowed from
# https://www.nylas.com/blog/use-python-requests-module-rest-apis/

def get_word():
    APIURL = 'https://random-word-api.herokuapp.com'
    res = requests.get(f'{APIURL}/word')
    try:        
        res.raise_for_status()
        return res.json()
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

def call_get_word():
    return get_word()[0]
