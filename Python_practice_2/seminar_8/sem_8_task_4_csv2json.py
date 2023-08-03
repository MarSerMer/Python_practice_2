# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import csv
import json

FILE_JSON = 'file_for_s8_task_4.json'
FILE_CSV = 'file_for_s8_task_3.csv'


def csv_to_json(csv_file: str = FILE_CSV, json_file: str = FILE_JSON) -> None:
    with open(csv_file, 'r', encoding='utf-8') as cf:
        csv_reader = csv.reader(cf, dialect='excel')
        data = []
        for i, row in enumerate(csv_reader):
            print(i, row)
            if i and (i % 2 == 0):
                level, user_id, name = row
                user_data = {}
                user_data['access_level'] = int(level)
                user_data['user_id'] = f'{int(user_id):010}'
                user_data['name'] = name.capitalize()
                user_data['hash'] = hash((user_id, name))
                data.append(user_data)
    with open(json_file, 'w', encoding='utf-8') as jf:
        json.dump(data, jf,indent=2,ensure_ascii=False)


csv_to_json()
