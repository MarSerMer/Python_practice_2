# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.

import json
from typing import Set
from sem_13_task_3_6_class_exc import LevelException, AccessException

FILE_OF_USERS = 'users.json'

# ЭТО преподаватель скинул в чат (штука для сериализации множества в json, используется в методе
# save_users_to_json.
class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

# data_str = json.dumps(set([1,2,3,4,5]), cls=SetEncoder)
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


class ProjectUser:
    def __init__(self, filename: str):
        self.admin_user = None
        self.filename = filename
        self.set_of_users = self.users_from_json()

    def users_from_json(self) -> Set[User]:
        with open(self.filename, 'r', encoding='utf-8') as jfr:
            dict_of_users: dict = json.load(jfr)
        set_of_users = set()
        for level, users in dict_of_users.items():
            for user_id, name in users.items():
                set_of_users.add(User(name, int(user_id), int(level)))
        return set_of_users

    # def enter_the_system(self) -> int | None:
    #     name = input('Please enter name of user: ')
    #     while True:
    #         user_id = input('Please enter user id: ')
    #         try:
    #             user_id = int(user_id)
    #             break
    #         except ValueError as e:
    #             print('User id should be an int number. Enter again: ')
    #     level = None
    #     for user in self.set_of_users:
    #         if user.name == name and user.user_id == user_id:
    #             level = user.level
    #             break
    #     if level == None:
    #         raise AccessException(level)
    #     return level

    def entrance(self, name: str, user_id: int):
        # Вот так это сделали на семинаре:
        test_user = User(name, user_id, 0)
        if test_user in self.set_of_users:
            for user in self.set_of_users:
                if test_user == user:
                    self.admin_user = user
        else:
            raise AccessException(test_user.level)

    def add_user_to_set(self, new_name: str, new_user_id: int, new_user_level: int):
        if new_user_level > self.admin_user.level:
            raise LevelException(self.admin_user, new_user_level)
        else:
            new_user = User(new_name, new_user_id, new_user_level)
            self.set_of_users.add(new_user)
            self.save_users_to_json()

    def save_users_to_json(self):
        dict_of_users:dict = {}
        for user in self.set_of_users:
            if user.level not in dict_of_users.keys():
                dict_of_users[user.level] = {}
                dict_of_users[user.level][user.user_id] = user.name
            else:
                dict_of_users[user.level][user.user_id] = user.name
        with open(self.filename, 'w', encoding='utf-8') as jfw:
            json.dump(dict_of_users,jfw,indent=2,sort_keys=True)
            # на семинаре так:
            # data = [{'name':user.name, 'user_id':user.user.id, 'access_level':user.level} for user in self.set_of_users]
            #json.dump(data, jfw, indent=2, ensure_ascii=False
            # мне так не нравится, нет защиты от повтора имен, оставлю как у меня было

if __name__ == '__main__':
    my_project = ProjectUser(FILE_OF_USERS)
    for user in my_project.set_of_users:
        print(user)
    my_project.entrance("Ttimm", 17)
    my_project.add_user_to_set('Korra', 28, 3)
    print('')
    for user in my_project.set_of_users:
        print(user)