"""
Задание 1.
Реализуйте функции:
a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import time


def operation_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения {func.__name__}: {round(end - start, 15)}')
        return res
    return wrapper


# Задание а
print('Задание а')
# Заполнение списка
@operation_time
def fill_list_append(count):
    example_list = []
    for i in range(count):
        example_list.append(i)          # O(1)


fill_list_append(100000)

@operation_time
def fill_list_insert(count):
    example_list = []
    for i in range(count):
        example_list.insert(0, i)       # O(n)


fill_list_insert(100000)

# Заполнение словаря
@operation_time
def fill_dict(count):
    example_dict = {}
    for i in range(count):
        example_dict[i] = i             # O(1)


fill_dict(100000)

# Заполнение списка(append) и словаря одинаковым количеством элементов с помощью цикла имеет одинаковую сложность
# операции: # O(n), но список заполняется немного быстрее, так как добавляется один элемент, а в словарь - пара
# элементов, также словарю необходимо преобразовать ключ в хеш


# Задание b
print('Задание b')
# Получение элементов списка
@operation_time
def elements_from_list(lst):
    for i in lst:
        a = i                           # O(1)


example_list = []
for i in range(100000):
    example_list.append(i)
elements_from_list(example_list)


# Получение элементов словаря
@operation_time
def elements_from_dict(dict):
    for k, v in dict.items():
        a, b = k, v                     # O(1)


example_dict = {}
for i in range(100000):
    example_dict[i] = i
elements_from_dict(example_dict)

# Получение элементов словаря дольше, так как возвращается два элемента


# Задание c
print('Задание с')
# Удаление элементов из списка
@operation_time
def delete_from_list(lst, number):
    for i in range(number):
        lst.pop(i)                      # O(n)


delete_from_list(example_list, 10000)


# Удаление элементов из словаря
@operation_time
def delete_from_dict(dict, number):
    for i in range(number):
        dict.pop(i)                     # O(1)


delete_from_dict(example_dict, 10000)

# Удаление элементов из словаря происходит путем обращения по ключу
