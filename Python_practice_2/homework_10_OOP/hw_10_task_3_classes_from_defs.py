# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
# которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра.

# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import json
import csv

FILE_JSON = r'C:\Users\User\Desktop\Geek Brains\16 Погружение в PYTHON\Python_practice_2\seminar_8\file_for_s8_task_2.json'
FILE_CSV = 'file_for_hw_10_task_3.csv'

class ConvertToCSV:
    def __init__(self, json_file: str, csv_file:str):
        self.json_f= json_file
        self.csv_f = csv_file

    def json_to_csv(self):
        with open(self.json_f, 'r', encoding='utf-8') as jfr:
            dict_of_users: dict = json.load(jfr)
        rows = []
        for level, users in dict_of_users.items():
            for user_id, name in users.items():
                rows.append({'level': int(level), 'id': int(user_id), 'name': name})
        with open(self.csv_f, 'w', encoding='utf-8') as cfw:
            csv_write = csv.DictWriter(cfw, fieldnames=['level', 'id', 'name'], dialect='excel')
            csv_write.writeheader()
            csv_write.writerows(rows)

if __name__ == "__main__":
    conv = ConvertToCSV(FILE_JSON,FILE_CSV)
    conv.json_to_csv()