# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv
import pickle

def csv2pickle(csv_file_path)->None:
    with open(csv_file_path,'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f,dialect='excel')
        data = []
        headers = []
        for i,row in enumerate(csv_reader):
            if not i:
                headers = row
            else:
                row_data = {key:value for key, value in zip(headers,row)}
                data.append(row_data)
    print(pickle.dumps(data))

csv2pickle('file_for_s8_task_6.csv')