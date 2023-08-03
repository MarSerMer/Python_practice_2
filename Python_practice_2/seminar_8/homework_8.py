# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import os
import pathlib
import json
import csv
from typing import Iterator
import pickle

DIR = r'C:\Users\User\Desktop\Geek Brains\16 Погружение в PYTHON\Python_practice_2\seminar_8'


def get_info_about_dir(dir: str = DIR) -> None:
    os.chdir(dir)
    all_in_dir = ((dir_path, dir_name, file_name) for (dir_path, dir_name, file_name) in os.walk(dir))
    list_of_all_in_dir: list = []
    for inf in all_in_dir:
        list_of_all_in_dir.append(inf)
        # print(inf)
    dict = {}
    for l in list_of_all_in_dir:
        for dr in l[1]:
            dict[f'{dr} from {l[0]}'] = {'type=': 'directory', 'parent=': l[0], 'size': os.path.getsize(dr)}
        for fl in l[2]:
            dict[f'{fl} from {l[0]}'] = {'type=': 'file', 'parent=': 'no parent', 'size': os.path.getsize(fl)}
    dict[f'{list_of_all_in_dir[0][0]} has no parent'] = {'type=': 'directory',
                                                         'parent=': 'no parent',
                                                         'size': os.path.getsize(dir)}
    for item in dict.items():
        print(item)
    with open ('homework_8.json','w', encoding='utf-8') as json_write:
        json.dump(dict, json_write, indent=2, ensure_ascii=False)
    for_csv = []
    for filename, fileinfo in dict.items():
        dict_for_csv: dict = {}
        dict_for_csv['object'] = filename
        dict_for_csv.update(**fileinfo)
        for_csv.append(dict_for_csv)
    headers = []
    for keys in for_csv[0].keys():
        headers.append(keys)
    with open ('homework_8.csv', 'w', encoding='utf-8') as csv_write:
        csv_wr = csv.DictWriter(csv_write, fieldnames=headers, dialect='excel-tab',quoting=csv.QUOTE_NONNUMERIC)
        csv_wr.writeheader()
        csv_wr.writerows(for_csv)
    with open ('homework_8.pickle','wb') as pickle_write:
        pickle.dump(for_csv, pickle_write)

        

if __name__ == '__main__':
    get_info_about_dir('.')
