"""
Задание 7. На закрепление навыков работы с деком
В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов,
например, 'топот'
Но могут быть и такие палиндромы, как 'молоко делили ледоколом'
Вам нужно доработать программу так, чтобы она могла выполнить
проверку на палиндром и в таких строках (включающих пробелы)
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--код с нуля писать не нужно, требуется доработать пример с урока
"""


class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


def check_palendrom(string):
    correct_string = string.replace(' ', '').lower()
    example = DequeClass()
    for i in correct_string:
        example.add_to_rear(i)
    while example.size() > 1:
        first_letter = example.remove_from_rear()
        last_letter = example.remove_from_front()
        if first_letter != last_letter:
            return False
    return True


print(check_palendrom('молоко делили ледоколом'))
print(check_palendrom('Лепс спел'))
print(check_palendrom('Здравствуйте'))
print(check_palendrom('ШАлаШ'))