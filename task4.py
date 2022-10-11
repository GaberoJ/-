"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
users = {
    'Artur': {'password': 4133, 'access': True},
    'Petr': {'password': 1532, 'access': False},
    'Denis': {'password': 1246, 'access': True},
    'Victor': {'password': 1636, 'access': True},
    'Alena': {'password': 8665, 'access': False}
}


# Алгоритм 1. Сложность O(1)
def check_access_first(diction, username, password):
    if diction[username]['access']:                                                 # O(1)
        if password == diction[username]['password']:                               # O(1)
            print('Заходите!')                                                      # O(1)
        else:                                                                       # O(1)
            print('Неверный пароль')                                                # O(1)
    else:                                                                           # O(1)
        print('Отказано в доступе, пожалуйста, активируйте свой аккаунт')           # O(1)


# Алгоритм 1. Сложность O(n)
def check_access_second(diction, username, password):                               # O(1)
    for k, v in diction.items():                                                    # O(n)
        if diction[username]['access']:                                             # O(1)
            if k == username and v['password'] == password:                         # O(1)
                return f'Заходите!'                                                 # O(1)
            else:                                                                   # O(1)
                return f'Неверный пароль!'                                          # O(1)
        else:                                                                       # O(1)
            return f'Отказано в доступе, пожалуйста, активируйте свой аккаунт'      # O(1)


check_access_first(users, 'Artur', 4133)
check_access_first(users, 'Petr', 4133)
check_access_first(users, 'Victor', 8665)
print(100 * '*')

print(check_access_second(users, 'Artur', 4133))
print(check_access_second(users, 'Petr', 4133))
print(check_access_second(users, 'Victor', 8665))

"""
Лучший из представленных вариантов - первый, так как он имеет меньшую вычислительную сложность
и не включает в себя циклы
"""
