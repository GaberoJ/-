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
from collections import defaultdict

dict_of_nums = defaultdict(list)
sum_nums = []
mul_nums = []
for i in range(1, 3):
    user_num = input('Введите число: ')
    for el in user_num:
        dict_of_nums[i].append(el.upper())

a = hex(int(''.join(dict_of_nums[1]), 16))[2:]
b = hex(int(''.join(dict_of_nums[2]), 16))[2:]

for el in (hex(int(a, 16) + int(b, 16))[2:]).upper():
    sum_nums.append(el)

for el in (hex(int(a, 16) * int(b, 16))[2:]).upper():
    mul_nums.append(el)

print(f'Сумма чисел: {sum_nums}')
print(f'Произведение чисел: {mul_nums}')

# Хранение данных
# print(dict_of_nums)










