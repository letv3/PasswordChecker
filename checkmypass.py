import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if (code := res.status_code) != 200:
        raise RuntimeError(f'Error fetching {code}, check the API and try again!')
    return res

def read_res(response):
    print(response.text)

def pwned_api_check(password):
    #check if password exitsts in API response
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1pass[:5], sha1pass[5:]
    res = request_api_data(first5)
    print(res)
    return res

pwned_api_check('1234234')