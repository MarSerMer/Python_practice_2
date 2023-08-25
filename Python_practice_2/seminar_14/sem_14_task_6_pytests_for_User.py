# Задание №6
# На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import pytest
from seminar_13_Exceptions.sem_13_task_5_class_User_improved import User, ProjectUser
from seminar_13_Exceptions.sem_13_task_3_6_class_exc import LevelException, AccessException

@pytest.fixture()
def new_set():
    user_set = {User('Maria',12,7),
          User('Dmitry', 14,4),
          User('Alex', 15,3)}
    return user_set

def test_user_entrance(new_set):
    project = ProjectUser('file_for_sem_14_task_6_(users).json')
    res = project.users_from_json()
    assert res == new_set

if __name__ == '__main__':
    pytest.main(['-v'])
