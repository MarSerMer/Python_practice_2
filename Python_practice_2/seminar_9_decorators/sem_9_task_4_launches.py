# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

from typing import Callable
from random import randint
from functools import wraps

def deco_launches(num_of_launches:int):
    res = []
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_of_launches):
                res.append(func(*args,**kwargs))
            return res
        return wrapper
    return deco


@deco_launches(15)
def sum_params()->int:
    res = 0
    for _ in range(5):
        res = res + randint(0,15)
    return res


if __name__ == '__main__':
    print(sum_params())