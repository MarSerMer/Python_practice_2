# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1

from  math import factorial

class GenForFactorial:
    def __init__(self, stop: int, start:int = 1, step:int = 1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            f = factorial(self.start)
            self.start += self.step
            return f
        raise StopIteration

    def __str__(self):
        res = f''

if __name__ == '__main__':
    fa = GenForFactorial(6,2,2)
    print(*fa)