from memory_profiler import profile, memory_usage
import time

"""
Код взят из курса Алгоритмы и структура данных (3 урок 1 задание)
"""


def operation_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        m1 = memory_usage()
        res = func(*args, **kwargs)
        m2 = memory_usage()
        end = time.time()
        print(f'Время выполнения {func.__name__}: {round(end - start, 15)}')
        print(m2[0] - m1[0])
        return res
    return wrapper


# @operation_time
# @profile
# def fill_list_append(count):
#     example_list = []
#     for i in range(count):
#         example_list.append(i)
#
#
# fill_list_append(10000)

# ------------------------------------------Оптимизация----------------------------------------------------------------
@operation_time
@profile
def fill_list_append(count):
    a = (i for i in range(10000))


fill_list_append(10000)

"""
Неоптимизированный код
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    18     19.8 MiB     19.8 MiB           1   @operation_time
    19                                         @profile
    20                                         def fill_list_append(count):
    21     19.8 MiB      0.0 MiB           1       example_list = []
    22     20.3 MiB      0.0 MiB       10001       for i in range(count):
    23     20.3 MiB      0.5 MiB       10000           example_list.append(i)
=============================================================
"""

"""
Оптимизированный код
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    29     19.8 MiB     19.8 MiB           1   @operation_time
    30                                         @profile
    31                                         def fill_list_append(count):
    32     19.8 MiB      0.0 MiB           2       a = (i for i in range(10000))
=============================================================
"""

# Данная оптимизация подойдет, если необходимо будет производить действия с каждым елементом списка
