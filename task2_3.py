"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
3) с помощью встроенной функции поиска медианы
сделайте замеры на массивах длиной 10, 100, 1000 элементов
В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from random import randint
from statistics import median
from timeit import timeit


def find_median(lst):
    return median(lst)


m = 10
my_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(timeit('find_median(my_list[:])', globals=globals(), number=100))

m = 100
my_list2 = [randint(0, 100) for _ in range(2 * m + 1)]
print(timeit('find_median(my_list2[:])', globals=globals(), number=100))

m = 1000
my_list3 = [randint(0, 100) for _ in range(2 * m + 1)]
print(timeit('find_median(my_list3[:])', globals=globals(), number=100))

"""
7.410001126118004e-05
0.0008675999997649342
0.01599700000951998
"""

# Самый эффективный способ для нахождения медианы массива - встроенная функция