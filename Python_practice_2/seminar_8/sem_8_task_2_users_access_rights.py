# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключом для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться

import json
import os

JSON_FILE: str = 'file_for_s8_task_2.json'
DICT_OF_USERS: dict = {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}}

all_entered_id: list = []


def check_level(level: str) -> bool:
    if int(level) < 1 or int(level) > 7:
        print('Wrong level value.')
    return 0 < int(level) < 8


def check_id(id: str) -> bool:
    global all_entered_id
    if id in all_entered_id:
        print('This id is already used.')
        return False
    else:
        all_entered_id.append(id)
        return True


def users_access_rights(json_file: str = JSON_FILE, dict_of_users: dict = None) -> None:
    if dict_of_users is None:
            dict_of_users = DICT_OF_USERS
    with open(json_file, 'a') as jf:
        while True:
            name, id, level = input('Please enter name, id, level of access over space: ').split()
            if not (check_level and check_id):
                continue
            dict_of_users[level] = [id, level]

def add_data_to_json(json_file:str = JSON_FILE):
    """Вот так это задание выполнили на семинаре"""
    users_ids = set()
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf=8') as jfr:
            data = json.load(jfr)
            for level in data.values():
                users_ids.update(level.keys())
    else:
        data:dict = {str(level):dict() for level in range(1,8)}
    while True:
        name = input('Enter your name: ')
        if not name:
             break
        id = input('Enter id: ')
        if id in users_ids:
            print('This id is already used.')
            continue
        else:
            users_ids.update(id)
        level = input('Enter access level: ')
        if not 0<int(level)<8:
            print('Wrong level value.')
            continue
        data[level][id] = name
        with open(json_file, 'w', encoding='utf-8') as jfw:
            json.dump(data,jfw,indent=2,sort_keys=True)

add_data_to_json(JSON_FILE)