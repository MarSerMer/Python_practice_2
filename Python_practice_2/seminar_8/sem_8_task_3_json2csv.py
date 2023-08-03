# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import json
import csv

FILE_JSON = 'file_for_s8_task_2.json'
FILE_CSV = 'file_for_s8_task_3.csv'


def json_to_csv(file_json: str = FILE_JSON, file_csv: str = FILE_CSV) -> None:
    with open(file_json, 'r', encoding='utf-8') as jfr:
        dict_of_users: dict = json.load(jfr)
    rows = []
    for level, users in dict_of_users.items():
        for user_id, name in users.items():
            rows.append({'level': int(level), 'id': int(user_id), 'name': name})
    with open(file_csv, 'w', encoding='utf-8') as cfw:
        csv_write = csv.DictWriter(cfw, fieldnames=['level', 'id', 'name'], dialect='excel')
        csv_write.writeheader()
        csv_write.writerows(rows)



if __name__ == '__main__':
    json_to_csv()
