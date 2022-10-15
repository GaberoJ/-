"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit

lst = []
deque_lst = deque()
cnt = 1000

def append_list(cnt):
    for i in range(cnt):
        lst.append(i)


def append_deque(cnt):
    for i in range(cnt):
        deque_lst.append(i)


def pop_list(cnt):
    for i in range(cnt):
        lst.pop()

def pop_deque(cnt):
    for i in range(cnt):
        deque_lst.pop()

def extend_list(lst):
    for i in range(cnt):
        lst.extend([0, 1, 2, 3, 4])

def extend_deque(deq):
    for i in range(cnt):
        deq.extend([0, 1, 2, 3, 4])


# Задание 1
print('Задание 1')
print('append_list', timeit('append_list(cnt)', globals=globals(), number=10000))
print('append_deque', timeit('append_deque(cnt)', globals=globals(), number=10000))
print('pop_list', timeit('pop_list(cnt)', globals=globals(), number=10000))
print('pop_deque', timeit('pop_deque(cnt)', globals=globals(), number=10000))
print('extend_list', timeit('extend_list(lst)', globals=globals(), number=10000))
print('extend_deque', timeit('extend_deque(deque_lst)', globals=globals(), number=10000), '\n')

# В случаях append, pop, extend  deque и list показывают примерно одинаковые результаты выполнения кода по времени.

# Задание 2
print('Задание 2')
lst.clear()
deque_lst.clear()
def append_left_list(cnt):
    for i in range(cnt):
        lst.insert(0, i)


def append_left_deque(cnt):
    for i in range(cnt):
        deque_lst.appendleft(i)


def pop_left_list(cnt):
    for i in range(cnt):
        lst.pop(0)


def pop_left_deque(cnt):
    for i in range(cnt):
        deque_lst.popleft()


def extend_left_list(lst):
    for i in range(100):
        for el in [0, 1, 2, 3, 4, 5, 6]:
            lst.insert(0, el)


def extend_left_deque(deq):
    for i in range(100):
        a = [0, 1, 2, 3, 4, 5, 6]
        deq.extendleft(a)


print('append_left_list', timeit('append_left_list(cnt)', globals=globals(), number=100))
print('append_left_deque', timeit('append_left_deque(cnt)', globals=globals(), number=100))
print('pop_left_list', timeit('pop_left_list(cnt)', globals=globals(), number=100))
print('pop_left_deque', timeit('pop_left_deque(cnt)', globals=globals(), number=100))
print('extend_left_list', timeit('extend_left_list(lst)', globals=globals(), number=100))
print('extend_left_deque', timeit('extend_left_deque(deque_lst)', globals=globals(), number=100), '\n')

# В случаях, когда необходимо производить действия с началом массива, гораздо лучше будет пользоваться deque, это
# видно из замеров.


# Задание 3
print('Задание 3')
def el_from_list(lst):
    for i in range(len(lst)):
        a = lst[i]

def el_from_deque(deq):
    for i in range(len(deq)):
        a = deq[i]

print('el_from_list', timeit('el_from_list(lst)', globals=globals(), number=100))
print('el_from_deque', timeit('el_from_deque(deque_lst)', globals=globals(), number=100))

# Для получения элемента следует использовать list, скорость выполнения операции выше, чем для deque









