# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class MyException(Exception):
    pass

class LevelException(MyException):

    def __str__(self):
        return 'Your level is less than the level of new user.'


class AccessException(MyException):
    def __init__(self,level):
        self.level = level

    def __str__(self):
        if self.level == None or self.level == 0:
            return 'User not found. Access denied.'
