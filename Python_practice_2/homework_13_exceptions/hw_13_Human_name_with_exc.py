from enum import Enum
from hw_13_exceptions import HumanNameException


class Gender(Enum):
    male = 'male'
    female = 'female'


class Name:
    """
    Helps to avoid entering wrong names.
    """
    def __init__(self, min_l: int = 1, max_l: int = 40):
        self.min_l = min_l
        self.max_l = max_l

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not self.min_l <= len(value) <= self.max_l:
            raise HumanNameException(value, self.min_l, self.max_l)


class HumanHomework13:
    name = Name(3, 15)
    patr_name = Name(7, 18)
    last_name = Name(1, 17)

    def __init__(self, name: str, patr_name: str, last_name: str, age: int, gender: Gender):
        self.name = name
        self.patr_name = patr_name
        self.last_name = last_name
        self._age = age
        self.gender = gender

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def full_name(self) -> str:
        return f'{self.last_name} {self.name} {self.patr_name}'

if __name__ == '__main__':
    test_human_1 = HumanHomework13('Alexey', 'Petrovich', 'Ivantsov', 15, Gender.male)
    print(test_human_1)
    test_human_2 = HumanHomework13('A', 'Petrovich', 'Ivantsov', 15, Gender.male)