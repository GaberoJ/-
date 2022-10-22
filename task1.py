"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
import random
from timeit import timeit


def bubble_sort_reverse(lst):
    print(f'Исходный массив: {lst}')
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    print(f'Отсортированный массив: {lst}')


def bubble_sort_reverse_update(lst):
    print(f'Исходный массив: {lst}')
    n = 1
    while n < len(lst):
        m = 0
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                m = 1
        if m == 0:
            break
        n += 1
    print(f'Отсортированный массив: {lst}')


check_list = [random.randint(-100, 100) for i in range(10000)]

print('Затраченное время: ', timeit('bubble_sort_reverse(check_list[:])', globals=globals(), number=1), '\n')

print('Затраченное время: ', timeit('bubble_sort_reverse_update(check_list[:])', globals=globals(), number=1))

# Исходя из полученного времени, можно сделать вывод, что использовать доработанный алгоритм нет смысла
