# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

from typing import Callable
import json
from os.path import exists
from functools import wraps


# def deco_info_to_json(func: Callable)->Callable[[int],int]:
def deco_info_to_json(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_name = f'task_3_{func.__name__}.json'
        data = []
        if exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as jf:
                data = json.load(jf)
        result = func(*args, **kwargs)
        func_info = {'positional parameters: ': (args),
                     **kwargs,
                     'result: ': result, }
        data.append(func_info)
        with open(file_name, 'w', encoding='utf-8') as jf:
            json.dump(data, jf,indent=2,ensure_ascii=False)
        return result
    return wrapper


@deco_info_to_json
def sum_params(*args,**kwargs)->int:
    return sum(args) + sum(value for value in kwargs.values())


if __name__ == '__main__':
    sum_params(7,3,2,h=3,f=5)
    sum_params(8,2,1,h=4,f=5)