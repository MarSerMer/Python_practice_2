# Напишите функцию группового переименования файлов. Она должна:
# -  принимать параметр желаемое конечное имя файлов.
#        При переименовании в конце имени добавляется порядковый номер.
#  - принимать параметр количество цифр в порядковом номере.
#  - принимать параметр расширение исходного файла.
#        Переименование должно работать только для этих файлов внутри каталога.
#  - принимать параметр расширение конечного файла.
#  - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
#        берутся буквы с 3 по 6 из исходного имени файла.
#        К ним прибавляется желаемое конечное имя, если оно передано.
#        Далее счётчик файлов и расширение.
# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

import os
from seminar_7 import sem_7_task_6_create_to_dir as s7_6

def get_number(number: int, digits_in_number: int) -> str:
    n = str(number)
    if len(n) < digits_in_number:
        zeros: str = '0' * (digits_in_number - len(n))
        n = f'{zeros}{n}'
    return n

def get_range_of_last_name(name:str, range_:list)->str:
    if len(name) > (range_[1]-range_[0]):
        name = name[range_[0]:range_[1]+1]
    return  name

def rename_many_files(*, new_name: str = '',
                      digits_in_number: int = 3,
                      ext: str = None,
                      final_ext: str,
                      range_: list = None) -> None:
    lst_of_files = os.listdir()
    number = 1
    for f in lst_of_files:
        if ext != None and not f.endswith(ext):
            continue
        last_name = ''
        if range_ != None:
            last_name = get_range_of_last_name(f, range_)
        num = get_number(number, digits_in_number)
        res_name = f'{last_name}{new_name}{num}.{final_ext}'
        os.rename(f, res_name)
        number += 1

if __name__ == '__main__':
    rename_many_files(new_name='ha-ha',digits_in_number=5,ext='jpeg',final_ext='bmp',range_=[0,1])

