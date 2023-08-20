# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

import json
from typing import Set
from sem_13_task_3_6_class_exc import LevelException, AccessException

FILE_OF_USERS = r'C:\Users\User\Desktop\Geek Brains\16 Погружение в PYTHON\Python_practice_2\seminar_8\file_for_s8_task_2.json'

class User:
    def __init__(self, name: str, user_id: int, level: int):
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'{self.name} has id: {self.user_id} and has access level {self.level}'

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id

    def __hash__(self):
        return hash((self.name, self.user_id))
def create_Users_from_json(filename:str = FILE_OF_USERS)->Set[User]:
    with open(filename, 'r', encoding='utf-8') as jfr:
        dict_of_users: dict = json.load(jfr)
    set_of_users = set()
    for level, users in dict_of_users.items():
        for user_id, name in users.items():
            set_of_users.add(User(name,user_id,level))
    return set_of_users

if __name__ == '__main__':
    set_of_users = create_Users_from_json()
    for user in set_of_users:
        print(user)
