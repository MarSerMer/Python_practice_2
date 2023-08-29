# Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

import logging
from typing import Callable

FORMAT = '{levelname} - {asctime} - {msg}'

logging.basicConfig(filename='file_for_task_3_args_res.log', encoding='utf-8',
                    level=logging.INFO, format=FORMAT, style='{')

logger = logging.getLogger(__name__)

def log_args_and_res(func: Callable):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        dict_to_log = {'args': args,
                       **kwargs,
                       'result"': res}
        log_msg = f'{func.__name__}: {dict_to_log}'
        logger.info(log_msg)
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