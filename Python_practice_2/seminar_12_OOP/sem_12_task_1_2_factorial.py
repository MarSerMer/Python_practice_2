# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

from collections import deque
import json

class CountFactorial:

    def __init__(self, k:int):
        self._history = deque(maxlen=k)

    def __call__(self, num:int):
        mul_num = 1
        for i in range (2, num +1):
            mul_num *= i
        self._history.append({num:mul_num})
        return mul_num

    def __str__(self):
        res = ''
        for v in self._history:
            res = f'{res}\n{v}'
        return res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        res = {}
        while self._history: # это фишка deque, цикл будет пробегать по всей очереди, пока она не закончится и не выдаст None
            res.update(self._history.popleft())
        with open('file_for_task_2.json', 'w', encoding='utf-8') as jw:
            json.dump(res,jw)


if __name__ == '__main__':
    counter = CountFactorial(3)
    with counter as c:
        print(c(10))
        print(c(5))
        print(c(8))
        print(c(40))
        print(c._history)
