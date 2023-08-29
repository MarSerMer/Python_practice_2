# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename='file_for_task_1_logging.log', encoding='utf-8', level=logging.ERROR)

def division(a: int, b: int) -> float:
    try:
        res = round(a/b,3)
    except ZeroDivisionError as e:
        logging.error(f'Внимание! Попытка деления на ноль!\n{e}')
        res = float('inf')
    return  res

if __name__ == '__main__':
    print(division(3, 10))
    print(division(3,0))