"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit


# Через цикл
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Через list comprehension
def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


# Через генератор
def func_3(nums):
    new_arr = []
    a = (i for i in range(len(nums)) if nums[i] % 2 == 0)
    for i in a:
        new_arr.append(i)
    return new_arr


n = [i for i in range(10000)]

print(timeit('func_1(n)', globals=globals(), number=1000))
print(timeit('func_2(n)', globals=globals(), number=1000))
print(timeit('func_3(n)', globals=globals(), number=1000))

# Самое быстрое решение через list comprehension. В отличае от простого цикла, отсутствует
# append на который также тратится время. Самое долгое решение через генератор, так как тратится
# время на саму генерацию, после чего цикл проходится по списку и с помощью append вносит значение в результирующий
# список

# Для проверки правильности работы функций
# print(func_1(n))
# print(func_2(n))
# print(func_3(n))
