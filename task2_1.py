"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
import random
from timeit import timeit


def gnome_sort(lst):
    index = 1
    i = 0
    while i < len(lst) - 1:
        if lst[i] < lst[i + 1]:
            i, index = index, index + 1
        else:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            i = i - 1
            if i < 0:
                i, index = index, index + 1
    return lst[len(lst) // 2]


m = 10
my_list = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(timeit('gnome_sort(my_list[:])', globals=globals(), number=100))

m = 100
my_list1 = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(timeit('gnome_sort(my_list1[:])', globals=globals(), number=100))

m = 1000
my_list2 = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(timeit('gnome_sort(my_list2[:])', globals=globals(), number=100))

"""
0.0024284999817609787
0.19820129999425262
26.036969899985706
"""