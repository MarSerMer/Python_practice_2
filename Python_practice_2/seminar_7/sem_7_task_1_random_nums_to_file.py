# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
import random
MIN_NUM = -1000
MAX_NUM = 1000

def add_random_nums_to_file(filename: str, amount: int):
    count = 0
    with open(filename, 'a') as f:
        while count < amount:
            str_to_file = f'{str(random.randint(MIN_NUM, MAX_NUM))}|{str(random.uniform(MIN_NUM, MAX_NUM))}\n'
            f.write(str_to_file)
            count += 1


if __name__ == "__main__":
    add_random_nums_to_file('file_for_s7_task_1', 12)