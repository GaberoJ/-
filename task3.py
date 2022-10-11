"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


companies = {
    'Sinopec Group': 410860,
    'State Grid': 386617,
    'Apple Inc.': 386080,
    'Amazon Inc.': 477750,
    'Exxon Mobil': 312710,
    'Walmart': 576010,
    'CVS Health': 299710
}


# Алгоритм 1. Сложность O(n^3)
def top_3_first(dict):
    top_3_companies = []                                                        # O(1)
    max_profit = [0]                                                            # O(1)
    for name, profit in dict.items():                                           # O(n)
        for el in max_profit:                                                   # O(n)
            if profit > el and profit not in max_profit:                        # O(n)
                max_profit.append(profit)                                       # O(1)
                if len(max_profit) > 3:                                         # O(1)
                    max_profit.remove(min(max_profit))                          # O(n)
    for name, profit in dict.items():                                           # O(n)
        if profit in max_profit:                                                # O(n)
            top_3_companies.append((name, profit))                              # O(1)
    return sorted(top_3_companies, reverse=True, key=lambda x: x[-1])           # O(n * logn)

# O(1) + O(1) + O(n) * O(n) * O(n) + O(1) + O(1) * O(n) + O(n) * O(n) + O(1) + O(n * logn) =
# = O(n^3) + O(n^2) + O(n * logn) + O(n) + O(1)


# Алгоритм 1. Сложность O(n * logn)
def top_3_second(dict):
    companies_list = sorted(list(dict.items()), reverse=True, key=lambda x: x[-1])         # O(n * logn)
    for i in range(0, 3):                                                                  # O(1)
        print(companies_list[i][0], ': ', companies_list[i][1])                            # O(1)


print(top_3_first(companies))
print(100 * '*')
top_3_second(companies)


"""
Лучший из представленных вариантов - второй, так как он имеет меньшую вычислительную сложность
и в целом более компактен и понятен.
"""






