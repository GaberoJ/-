from random import choice
from memory_profiler import profile
from collections import namedtuple

"""
Код взят из курса Основы Python (3 урок 5 задание)
"""

# @profile
# def get_jokes(count):
#     """Return the selected number of jokes."""
#
#     jokes = []
#     nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
#     adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
#     adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#     for i in range(5000):
#         for i in range(count):
#             nouns_string, adverbs_string, adjectives_string = (choice(nouns)), (choice(adverbs)), (choice(adjectives))
#             jokes.append(f'{nouns_string} {adverbs_string} {adjectives_string}')
#     print(jokes[1])
#     return jokes
#
#
# get_jokes(5)


# ------------------------------------------Оптимизация----------------------------------------------------------------

@profile
def get_jokes2(count):
    """Return the selected number of jokes."""

    a = namedtuple('Joke', 'noun adverbs adjectives')
    jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(5000):
        for i in range(count):
            jokes.append(a(choice(nouns), choice(adverbs), choice(adjectives)))
    print(' '.join(jokes[1]))
    return jokes


get_jokes2(5)


"""
Неоптимизированный код
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     5     19.8 MiB     19.8 MiB           1   @profile
     6                                         def get_jokes(count):
     7                                             Return the selected number of jokes.
     8                                         
     9     19.8 MiB      0.0 MiB           1       jokes = []
    10     19.8 MiB      0.0 MiB           1       nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    11     19.8 MiB      0.0 MiB           1       adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    12     19.8 MiB      0.0 MiB           1       adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    13     22.9 MiB      0.0 MiB        5001       for i in range(5000):
    14     22.9 MiB      1.4 MiB       30000           for i in range(count):
    15     22.9 MiB      0.0 MiB       25000               nouns_string, adverbs_string, adjectives_string = (choice(nouns)), (choice(adverbs)), (choice(adjectives))
    16     22.9 MiB      1.8 MiB       25000               jokes.append(f'{nouns_string} {adverbs_string} {adjectives_string}')
    17     22.9 MiB      0.0 MiB           1       print(jokes[1])
    18     22.9 MiB      0.0 MiB           1       return jokes
"""

"""
Оптимизированный код
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    26     19.7 MiB     19.7 MiB           1   @profile
    27                                         def get_jokes2(count):
    28                                             Return the selected number of jokes.
    29                                         
    30     19.8 MiB      0.0 MiB           1       a = namedtuple('Joke', 'noun adverbs adjectives')
    31     19.8 MiB      0.0 MiB           1       jokes = []
    32     19.8 MiB      0.0 MiB           1       nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    33     19.8 MiB      0.0 MiB           1       adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    34     19.8 MiB      0.0 MiB           1       adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    35     21.9 MiB      0.0 MiB        5001       for i in range(5000):
    36     21.9 MiB      0.0 MiB       30000           for i in range(count):
    37     21.9 MiB      2.2 MiB       25000               jokes.append(a(choice(nouns), choice(adverbs), choice(adjectives)))
    38     21.9 MiB      0.0 MiB           1       print(' '.join(jokes[1]))
    39     21.9 MiB      0.0 MiB           1       return jokes
"""

# Для оптимизации я использовал namedtuple, а также избавился от операций определения новых переменных.