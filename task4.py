"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

usual_dictionary = {}
ord_dictionary = OrderedDict()
cnt = 200

def add_dict(cnt):
    for i in range(cnt):
        usual_dictionary[i] = i

def add_ord_dict(cnt):
    for i in range(cnt):
        ord_dictionary[i] = i

def el_from_dict(cnt):
    for i in range(cnt):
        a = usual_dictionary[i]

def el_from_ord_dict(cnt):
    for i in range(cnt):
        a = ord_dictionary[i]

def pop_from_dict(cnt):
    for i in range(len(usual_dictionary)):
        usual_dictionary.pop(i)

def pop_from_ord_dict(cnt):
    for i in range(len(ord_dictionary)):
        ord_dictionary.pop(i)

def move_to_end_dict():
    for i in range(len(usual_dictionary)):
        a = usual_dictionary.pop(i)
        usual_dictionary[a] = i


def move_to_end_ord_dict():
    for i in range(len(ord_dictionary)):
        ord_dictionary.move_to_end(i, True)


print('add_dict', timeit('add_dict(cnt)', globals=globals(), number=100000))
print('add_ord_dict', timeit('add_ord_dict(cnt)', globals=globals(), number=100000))
print('el_from_dict', timeit('el_from_dict(cnt)', globals=globals(), number=100000))
print('el_from_ord_dict', timeit('el_from_ord_dict(cnt)', globals=globals(), number=100000))
print('pop_from_dict', timeit('pop_from_dict(cnt)', globals=globals(), number=100000))
print('pop_from_ord_dict', timeit('pop_from_ord_dict(cnt)', globals=globals(), number=100000))
add_dict(cnt)
add_ord_dict(cnt)
print('move_to_end_dict', timeit('move_to_end_dict()', globals=globals(), number=100000))
print('move_to_end_ord_dict', timeit('move_to_end_ord_dict()', globals=globals(), number=100000))


# Исходя из полученных замеров, можно сделать вывод, что OrderedDict будет полезен только в случае, когда нужно
# переместить элемент словаря в конец. Также OrderedDict можно использовать, для того, чтобы показать другим
# важность определенной последовательности.













