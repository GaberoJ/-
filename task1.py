"""
Задание 1.
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего
Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import namedtuple


def profit(comp):
    return comp.profit_1 + comp.profit_2 + comp.profit_3 + comp.profit_4


Companies = namedtuple('Companies', 'company profit_1 profit_2 profit_3 profit_4')
dict_of_companies = {}
sum_profit_for_all_companies = 0
lower_average_profit = []
upper_average_profit = []

num_of_companies = int(input('Введите количество предприятий: '))
for i in range(num_of_companies):
    new_company = Companies(
        company=input('Введите название компании: '),
        profit_1=int(input('Введите прибыль компании за 1 квартал: ')),
        profit_2=int(input('Введите прибыль компании за 2 квартал: ')),
        profit_3=int(input('Введите прибыль компании за 3 квартал: ')),
        profit_4=int(input('Введите прибыль компании за 4 квартал: '))
    )
    dict_of_companies.setdefault(i, new_company)
    sum_profit_for_all_companies += profit(new_company)
    print(f'\033[31mПрибыль компании {new_company.company}: {profit(new_company)}\033[0m')

average_profit_for_all_companies = sum_profit_for_all_companies / num_of_companies
for v in dict_of_companies.values():
    if profit(v) < average_profit_for_all_companies:
        lower_average_profit.append(v.company)
    else:
        upper_average_profit.append(v.company)

print(f'\nСредняя годовая прибыль всех предприятий: {average_profit_for_all_companies}\n')
print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(lower_average_profit)}')
print(f'Предприятия, с прибылью выше среднего значения: {", ".join(upper_average_profit)}')
