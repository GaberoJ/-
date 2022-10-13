"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв
Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""
import hashlib


def unique_substring(user_str):
    letter_set = set()
    hash_set = set()
    for i in range(len(user_str)):
        for j in range(len(user_str) + 1):
            if user_str[i:j] and len(user_str[i:j]) != len(user_str):
                letter_set.add(user_str[i:j])
                hash_set.add(hashlib.sha256(user_str[i:j].encode()).hexdigest())
    print(f'Уникальные подстроки: {letter_set}')
    print(f'Хэш уникальных подстрок: {hash_set}')
    print(f'Длина уникальных подстрок в {user_str}: {len(hash_set)}')


unique_substring('papa')
print(100 * '*')
unique_substring('artur')
