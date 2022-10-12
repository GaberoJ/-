"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def guess_the_number(computer_number, count=1):
    print(f'Попытка № {count}')
    user_number = int(input('Введите число: '))
    if user_number == computer_number:
        print(f'Вы угадали с {count} попытки!')
    elif count == 10:
        return print(f'К сожалению, вы потратили все 10 попыток. Загаданное число: {computer_number}')
    else:
        if user_number > computer_number:
            print('Ваше число больше загаданного')
            count += 1
        else:
            print('Ваше число меньше загаданного')
            count += 1
        return guess_the_number(computer_number, count)


num = random.randint(0, 100)
guess_the_number(num, 1)
