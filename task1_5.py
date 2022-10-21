from memory_profiler import profile

"""
Код взят из курса Основы Python (1 урок 2 задание)
"""

# @profile
# def sum_list_1(dataset: list) -> int:
#     summ_numbers = []
#     for i in range(1000):
#         for number in dataset:
#             summ = 0
#             number1 = number
#             while number1 != 0:
#                 summ += number1 % 10
#                 number1 = number1 // 10
#             if summ % 7 == 0 or summ % 3 == 0:
#                 summ_numbers.append(number)
#     total = sum(summ_numbers)
#     return total


# ------------------------------------------Оптимизация----------------------------------------------------------------

@profile
def sum_list_2(dataset: list) -> int:
    summ_numbers = 0
    for i in range(1000):
        for number in dataset:
            summ = 0
            number1 = number
            while number1 != 0:
                summ += number1 % 10
                number1 = number1 // 10
            if summ % 7 == 0 or summ % 3 == 0:
                summ_numbers += number
    return summ_numbers


my_list = [i for i in range(1, 100, 2)]

# print(sum_list_1(my_list))
print(sum_list_2(my_list))

"""
Неоптимизированный код
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     19.7 MiB     19.7 MiB           1   @profile
     5                                         def sum_list_1(dataset: list) -> int:
     6     19.7 MiB      0.0 MiB           1       summ_numbers = []
     7     20.1 MiB      0.0 MiB        1001       for i in range(1000):
     8     20.1 MiB      0.0 MiB       51000           for number in dataset:
     9     20.1 MiB      0.0 MiB       50000               summ = 0
    10     20.1 MiB      0.0 MiB       50000               number1 = number
    11     20.1 MiB      0.0 MiB      145000               while number1 != 0:
    12     20.1 MiB      0.0 MiB       95000                   summ += number1 % 10
    13     20.1 MiB      0.0 MiB       95000                   number1 = number1 // 10
    14     20.1 MiB      0.0 MiB       50000               if summ % 7 == 0 or summ % 3 == 0:
    15     20.1 MiB      0.4 MiB       24000                   summ_numbers.append(number)
    16     20.1 MiB      0.0 MiB           1       total = sum(summ_numbers)
    17     20.1 MiB      0.0 MiB           1       return total
"""


"""
Оптимизированный код
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    22     19.8 MiB     19.8 MiB           1   @profile
    23                                         def sum_list_2(dataset: list) -> int:
    24     19.8 MiB      0.0 MiB           1       summ_numbers = 0
    25     19.8 MiB      0.0 MiB        1001       for i in range(1000):
    26     19.8 MiB      0.0 MiB       51000           for number in dataset:
    27     19.8 MiB      0.0 MiB       50000               summ = 0
    28     19.8 MiB      0.0 MiB       50000               number1 = number
    29     19.8 MiB      0.0 MiB      145000               while number1 != 0:
    30     19.8 MiB      0.0 MiB       95000                   summ += number1 % 10
    31     19.8 MiB      0.0 MiB       95000                   number1 = number1 // 10
    32     19.8 MiB      0.0 MiB       50000               if summ % 7 == 0 or summ % 3 == 0:
    33     19.8 MiB      0.0 MiB       24000                   summ_numbers += number
    34     19.8 MiB      0.0 MiB           1       return summ_numbers
"""

# Данный код я оптимизировал путем замены списка на число, результат остался тем же, а использование памяти уменьшилось