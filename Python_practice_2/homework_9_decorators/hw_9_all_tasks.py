# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

from os.path import exists
from random import randint
import csv
from typing import Callable
import json

FILE_NAME = 'hw_9.csv'
F_NAME_JSON = 'hw_9_indexes_and_roots.json'
HOW_MANY_STRINGS_IN_FILE = 100
RANGE_FOR_NUMS = 40


def write_indexes_and_roots_to_json(file_name:str = F_NAME_JSON):
    def deco_info_to_json(func: Callable):
        def wrapper(*args, **kwargs):
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
    return deco_info_to_json
def make_comp_count_roots(file_name: str):
    res = []
    indexes = []
    with open(file_name, 'r', newline='') as f:
        csv_r = csv.reader(f, dialect='excel', delimiter=',')
        for line in csv_r:
            indexes.append(line)
    nums = []
    for i in range(len(indexes)):
        ind = [int(a) for a in indexes[i]]
        nums.append(ind)
    def deco(func: Callable):
        def wrapper():
            for ind_int in nums:
                roots = func(ind_int[0], ind_int[1], ind_int[2])
                res.append(roots)
            return res

        return wrapper

    return deco


@make_comp_count_roots(FILE_NAME)
@write_indexes_and_roots_to_json(F_NAME_JSON)
def count_roots(a: int = 0, b: int = 0, c: int = 0) -> tuple[float] | float | None:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x_1 = round((-b - d ** 0.5) / (2 * a), 4)
        x_2 = round((-b + d ** 0.5) / (2 * a), 4)
        result = (x_1, x_2)
    elif d == 0:
        x = round(-b / (2 * a), 4)
        result = x
    else:
        result = None
    return result


def generate_csv_file_witn_numbers(file_name: str = FILE_NAME):
    nums = []
    for _ in range(HOW_MANY_STRINGS_IN_FILE):
        three_nums = [randint(-RANGE_FOR_NUMS, RANGE_FOR_NUMS) for _ in range(3)]
        nums.append(three_nums)
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(nums)


if __name__ == '__main__':
    generate_csv_file_witn_numbers()
    count_roots()
