# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import os
import pickle
import json
import csv

FILE_NAME = 'file_for_s8_task_4.json'


def pickle2csv(pickle_file:str, csv_file_path: str) -> None:
    with open (pickle_file, 'rb') as pfr:
        data = pickle.load(pfr)
    headers = data[0].keys()
    with open (csv_file_path, 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers,
                                    dialect='excel',quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(data)

pickle2csv('file_for_s8_task_4.pickle', 'file_for_s8_task_6.csv')