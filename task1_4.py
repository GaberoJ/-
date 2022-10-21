from memory_profiler import profile
import random

"""
Код взят из курса Основы Python (5 урок 4 задание)
"""


# @profile
# def get_list():
#     src = [random.randint(0, 100) for i in range(100000)]
#     result = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
#     return result
#
#
# get_list()

# ------------------------------------------Оптимизация----------------------------------------------------------------


@profile
def get_list2():
    res = []
    src = (random.randint(0, 100) for i in range(100000))
    for i in src:
        last = next(src)
        if last > i:
            res.append(last)
    return res

get_list2()


"""
Неоптимизированный код
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     19.8 MiB     19.8 MiB           1   @profile
     5                                         def get_list():
     6     21.6 MiB      1.9 MiB      100003       src = [random.randint(0, 100) for i in range(100000)]
     7     21.6 MiB      0.0 MiB      100002       result = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
     8     21.6 MiB      0.0 MiB           1       return result
"""

"""
Оптимизированный код
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    16     19.7 MiB     19.7 MiB           1   @profile
    17                                         def get_list2():
    18     19.7 MiB      0.0 MiB           1       res = []
    19     20.0 MiB      0.0 MiB      200003       src = (random.randint(0, 100) for i in range(100000))
    20     20.0 MiB      0.0 MiB       50001       for i in src:
    21     20.0 MiB      0.0 MiB       50000           last = next(src)
    22     20.0 MiB      0.0 MiB       50000           if last > i:
    23     20.0 MiB      0.3 MiB       24839               res.append(last)
    24     20.0 MiB      0.0 MiB           1       return res
"""

# В данном коде оптимизация была достигнута путем замены LC на генератор