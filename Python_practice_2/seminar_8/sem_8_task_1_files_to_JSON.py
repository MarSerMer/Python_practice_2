# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json

FILENAME: str = r'C:\Users\User\Desktop\Geek Brains\16 Погружение в PYTHON\Python_practice_2\seminar_8\file_for_s7_task_3'
JSON_FILE: str = 'file_for_s8_task_1.json'

def file_to_JSON(filename: str = FILENAME, json_file: str = JSON_FILE):
    from_file: dict = {}
    with open (filename, 'r', encoding='utf-8') as f:
        while res := f.readline():
            list = res.split()
            from_file[list[0].capitalize()] = float(list[1])
    with open(json_file, 'w', encoding='utf-8') as jf:
        json.dump(from_file, jf, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    file_to_JSON()