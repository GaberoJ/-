"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте собственный класс-структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class Stack_of_plates:
    def __init__(self, max_plates_in_stack):
        self.stack = [[]]
        self.max_plates_in_stack = max_plates_in_stack

    def add_plates(self, count_of_plates):
        for i in range(count_of_plates):
            if len(self.stack[-1]) == self.max_plates_in_stack:
                self.stack.append([])
            self.stack[-1].append('plate')

    def show_stacks(self):
        for i in self.stack:
            print(i)
        return f'Всего {len(self.stack)} стопок. Максимальное число тарелок в одной стопке' \
               f' {self.max_plates_in_stack}. Число тарелок' \
               f' {(len(self.stack) - 1) * self.max_plates_in_stack + len(self.stack[-1])}'


mam = Stack_of_plates(5)
mam.add_plates(11)
mam.add_plates(6)
print(mam.show_stacks())
print(100 * '*')

dad = Stack_of_plates(8)
dad.add_plates(35)
print(dad.show_stacks())
