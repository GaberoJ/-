"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    revers_num = ''.join([str(enter_num)[-i] for i in range(1, len(str(enter_num)) + 1)])
    return revers_num


n = 54785
print(timeit('revers(n, revers_num=0)', globals=globals(), number=100000))
print(timeit('revers_2(n, revers_num=0)', globals=globals(), number=100000))
print(timeit('revers_3(n)', globals=globals(), number=100000))
print(timeit('revers_4(n)', globals=globals(), number=100000))

# Проверка моей функции
# print(revers_4(n))

# Функции по затратам времени (от самой быстрой, к самой медленной):
# 1) revers_3 - здесь не происходит никаких математических операций, а только преобразование в строку и срез.
# 2) revers_2 - здесь присутствуют математические операции и цикл, поэтому ф-я выполняется дольше  чем ф-я 1.
# 3) revers - здесь отсутствует цикл, но решение через рекурсию, следовательно ф-я будет выполняться несколько раз
#             для переданного аргумента.
# 4) revers_4 - здесь происходит большое количество операций: конкатинация, преобразование в строку, обращение
#               по индексу, цикл, определение длины. Хоть это решение и в 1 строчку, но такое количество производимых
#               операций 100000 раз уступает по времени остальным ф-м.
#
# Вывод: самая эффективная ф-я revers_3 (через срез), потому что она самая быстрая (т.к. она включает в себя минимальное
# количество операций), понятная, не требует много времени для написания и проверки.
