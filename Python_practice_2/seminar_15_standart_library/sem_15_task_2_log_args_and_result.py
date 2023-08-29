# Задание №2
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

import logging
from typing import Callable

logging.basicConfig(filename='file_for_task_2_args_res.log', encoding='utf-8', level=logging.INFO)

logger = logging.getLogger(__name__)

def log_args_and_res(func: Callable):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        dict_to_log = {'args':args,
                **kwargs,
                'result"':res}
        logger.info(dict_to_log)
        return res
    return wrapper

@log_args_and_res
def division(a: int, b: int) -> float:
    try:
        res = round(a/b,3)
    except ZeroDivisionError as e:
        res = float('inf')
    return  res

if __name__ == '__main__':
    print(division(10,2))