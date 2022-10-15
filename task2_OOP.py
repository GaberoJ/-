"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""


class Calculator16:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        sum_of_nums = []
        a = hex(int(self.num, 16) + int(other.num, 16))
        for el in a[2:]:
            sum_of_nums.append(el.upper())
        return f'Сумма чисел: {sum_of_nums}'

    def __mul__(self, other):
        mul_of_nums = []
        a = hex(int(self.num, 16) * int(other.num, 16))
        for el in a[2:]:
            mul_of_nums.append(el.upper())
        return f'Произведение чисел: {mul_of_nums}'


first = Calculator16(input('Введите первое число: '))
second = Calculator16(input('Введите второе число: '))
print(first + second)
print(first * second)
