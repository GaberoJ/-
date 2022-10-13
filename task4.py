"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib
from uuid import uuid4

salt = uuid4().hex
url_dict = {}


def url_checker(url):
    hash_url = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
    if url not in url_dict:
        url_dict[url] = hash_url
        print(f'В кэш добавлен URL {url}, хэш: {hash_url}')
    else:
        print(f'URL {url} есть в кэше, хеш: {hash_url}')


url_checker('https://www.google.ru/')
url_checker('https://ya.ru/')
url_checker('https://www.google.ru/')
