import json
from pympler import asizeof

"""
Код взят из курса Основы Python (3 урок 3 задание)
"""


def thesaurus(*args):
    """Creates a dictionary with names."""
    dict_of_names = {}
    """Creates a dictionary with names."""
    for name in args:
        if name[0] in dict_of_names:
            dict_of_names[name[0]].append(name)
        else:
            dict_of_names[name[0]] = [name]
    print(asizeof.asizeof(dict_of_names))
    return dict_of_names


thesaurus("Иван", "Мария", "Петр", "Илья", "Афанасий", "Авдотья", "Кирилл", "Артур", "Павел")


def thesaurus2(*args):
    dict_of_names2 = {}
    """Creates a dictionary with names."""
    for name in args:
        if name[0] in dict_of_names2:
            dict_of_names2[name[0]].append(name)
        else:
            dict_of_names2[name[0]] = [name]
    dumped_dict = json.dumps(dict_of_names2)
    print(asizeof.asizeof(dumped_dict))


thesaurus2("Иван", "Мария", "Петр", "Илья", "Афанасий", "Авдотья", "Кирилл", "Артур", "Павел")

# Код можно оптимизировать с помощью сериализации. Размер словаря до сериализции 1920, а после - 440 байт
