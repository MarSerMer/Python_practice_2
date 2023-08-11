# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from random import randint
from sem_10_task_3_human_info import Human, Gender


class Employee(Human):
    MAX_LEVEL = 7
    MIN_ID = 100_000
    MAX_ID = 999_999

    def __init__(self, name: str, patr_name: str, last_name: str, age: int, gender: Gender, emp_id: int):
        super().__init__(name, patr_name, last_name, age, gender)
        if self.MIN_ID<emp_id<=self.MAX_ID:
            self.emp_id = emp_id
        else:
            self.emp_id = randint(self.MIN_ID,self.MAX_ID)

    def get_level(self) -> int:
        nums_of_id = sum(int(n) for n in str(self.emp_id))
        return nums_of_id % self.MAX_LEVEL

emp_1 = Employee('Bob','---','Johnson',27,Gender.male, 777_777)
print(emp_1.get_level())
print(hash(emp_1))

emp_2 = Employee('Bob','---','Johnson',27,Gender.male, 777_777)
print(emp_1.get_level())
print(hash(emp_2))