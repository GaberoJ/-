"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


# Алгоритм 1. Сложность O(n^2)
def first_min_list(lst):
    number = lst[0]                         # O(1)
    for i in lst:                           # O(n)
        for j in lst:                       # O(n)
            if i < j and i < number:        # O(1)
                number = i                  # O(1)
    return number                           # O(1)


# Алгоритм 2. Сложность O(n)
def second_min_list(lst):
    number = lst[0]                         # O(1)
    for i in lst:                           # O(n)
        if i < number:                      # O(1)
            number = i                      # O(1)
    return number                           # O(1)


check_list = [12, 5, 3, 8, 210, 40]
print(first_min_list(check_list))
print(second_min_list(check_list))
