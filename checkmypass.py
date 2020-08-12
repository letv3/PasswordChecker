import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if (code := res.status_code) != 200:
        raise RuntimeError(f'Error fetching {code}, check the API and try again!')
    return res

# def read_res(response):
#     print(response.text)

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    #check if password exitsts in API response
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1pass[:5], sha1pass[5:]
    res = request_api_data(first5)
    return get_password_leaks_count(res,tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times, u should change')
        else:
            print(f'{password} was Not found')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))