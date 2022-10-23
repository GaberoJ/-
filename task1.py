"""
Задание 1.
Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
from collections import Counter
from collections import deque


class Haffman:
    def __init__(self, my_string):
        self.my_string = my_string

    def get_coded_string(self):
        sorted_deq = deque(sorted(Counter(self.my_string).items(), key=lambda item: item[1]))
        while len(sorted_deq) > 1:
            weight = sorted_deq[0][1] + sorted_deq[1][1]
            elem_dict = {0: sorted_deq.popleft()[0],
                         1: sorted_deq.popleft()[0]}
            for i, val in enumerate(sorted_deq):
                if weight > val[1]:
                    continue
                else:
                    sorted_deq.insert(i, (elem_dict, weight))
                    break
            else:
                sorted_deq.append((elem_dict, weight))

        res = {}

        def res_code(tree, path=''):
            if not isinstance(tree, dict):
                res[tree] = path
            else:
                res_code(tree[0], path=f'{path}0')
                res_code(tree[1], path=f'{path}1')

        res_code(sorted_deq[0][0])

        for i in self.my_string:
            print(res[i], end=' ')


STRING = 'beep boop beer!'

a = Haffman(STRING)
a.get_coded_string()
