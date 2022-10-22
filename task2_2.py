"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
import random
from timeit import timeit


def find_median(lst, cnt):
    for i in range(cnt):
        lst.pop(lst.index(max(lst)))
    return max(lst)


m = 10
my_list = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(timeit('find_median(my_list[:], m)', globals=globals(), number=100))

m = 100
my_list2 = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(timeit('find_median(my_list2[:], m)', globals=globals(), number=100))

m = 1000
my_list3 = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(timeit('find_median(my_list3[:], m)', globals=globals(), number=100))

"""
0.0005145999894011766
0.022949500009417534
2.015626300009899
"""