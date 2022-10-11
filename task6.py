"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class TaskBoard:
    def __init__(self):
        self.base_queue = []
        self.modification_queue = []
        self.done_queue = []

    def add_task(self, task):
        self.base_queue.insert(0, task)

    def task_to_modification(self):
        moving_task = self.base_queue.pop()
        self.modification_queue.insert(0, moving_task)

    def task_to_done(self):
        moving_task = self.base_queue.pop()
        self.done_queue.insert(0, moving_task)

    def from_modification_to_done(self):
        moving_task = self.modification_queue.pop()
        self.done_queue.insert(0, moving_task)


worker = TaskBoard()

worker.add_task('Сделать отчет')
worker.add_task('Пообедать')
worker.add_task('Покормить рыбок')
worker.add_task('Убраться на столе')
worker.add_task('Зайти к начальнику')
worker.add_task('Позвонить покупателю')

print(f'Базовый список: {worker.base_queue}')

worker.task_to_modification()
worker.task_to_modification()
worker.task_to_modification()

print(f'Базовый список после отправки задачи на доработку: {worker.base_queue}')
print(f'Список для доработки: {worker.modification_queue}')

worker.task_to_done()

print(f'Базовый список после выполненной задачи: {worker.base_queue}')
print(f'Список выполненных задач: {worker.done_queue}')

worker.from_modification_to_done()
worker.from_modification_to_done()

print(f'Список для доработки: {worker.modification_queue}')
print(f'Список выполненных задач: {worker.done_queue}')



