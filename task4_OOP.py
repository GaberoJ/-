import hashlib
import json
import pprint
from uuid import uuid4


class UrlChecker:
    def __init__(self):
        self.salt = uuid4().hex
        self.url_dict = {}

    def url_checker(self, url):
        self.url = url
        hash_url = hashlib.sha512(self.salt.encode() + url.encode()).hexdigest()
        if url not in self.url_dict:
            with open('password_hash.json', 'w') as f:
                self.url_dict[url] = hash_url
                print(f'В кэш добавлен URL {url}, хэш: {hash_url}')
                json.dump(self.url_dict, f)
        else:
            with open('password_hash.json', 'r') as f:
                json_data = json.load(f)
            print(f'URL {url} есть в кэше, хеш: {json_data[url]}')


user = UrlChecker()
user.url_checker('https://www.google.ru/')
user.url_checker('https://ya.ru/')
user.url_checker('https://www.google.ru/')
user.url_checker('https://ru.wikipedia.org/wiki/')
user.url_checker('https://ya.ru/')
print('\nКэш:')

with open('password_hash.json', 'r') as f:
    json_data = json.load(f)
pprint.pprint(json_data)
