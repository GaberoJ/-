"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
import json
import hashlib

# Запись в файл
with open('password_hash.json', 'w') as f:
    user_password = input('Введите пароль: ')
    salt = 'it`s salt'
    salt_hash = hashlib.sha256(salt.encode()).hexdigest()
    password_hash = (hashlib.sha256(user_password.encode())).hexdigest()
    info = {'salt_hash': salt_hash,
            'password_hash': (hashlib.sha256(salt.encode() + user_password.encode())).hexdigest()}
    print('Хэш пароля: ', (hashlib.sha256(salt.encode() + user_password.encode())).hexdigest())
    json.dump(info, f)

# Проверка
with open('password_hash.json', 'r') as f:
    json_data = json.load(f)

user_password_again = input('Повторите пароль: ')
if hashlib.sha256(salt.encode() + user_password_again.encode()).hexdigest() == json_data['password_hash']:
    print('Пароли совпадают')
else:
    print('Пароли не совпадают')
