# Создайте класс студента.
# ○ Используя дескрипторы: проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.

import csv
from statistics import mean

FILE_NAME = 'subjects.csv'
res_list = ['tests', 'scores']
SCORE_MIN = 2
SCORE_MAX = 5
TEST_MIN = 0
TEST_MAX = 100

class DescrName:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if value.isalpha():
            setattr(instance, self.name, value.capitalize())
        else:
            raise ValueError('There should be only letters in name.')

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Student:
    last_name: str = DescrName()
    first_name: str = DescrName()
    patr_name: str = DescrName()

    def __init__(self, last_name: str, first_name: str, patr_name: str):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        with open(FILE_NAME, 'r', newline='') as f:
            instance.subjects = []
            subjects = []
            csv_reader = csv.reader(f)
            for line in csv_reader:
                subjects.append(line)
            for word in subjects[0]:
                instance.subjects.append(word.capitalize())
            instance.__study_res = {}
            for word in instance.subjects:
                instance.__study_res[word.capitalize()] = {}
                for values in instance.__study_res.values():
                    for r in res_list:
                        values[r] = []
        return instance

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patr_name} \n {self.__study_res}'

    def write_score(self, subject: str, score: int):
        subject = subject.capitalize()
        if not SCORE_MIN <= score <= SCORE_MAX or not subject in self.subjects:
            raise ValueError(f'Score not between {SCORE_MIN} and {SCORE_MAX} or subject not in {self.subjects}')
        else:
            self.__study_res[subject]['scores'].append(score)

    def show_score_and_avg(self, subject: str):
        subject = subject.capitalize()
        if not subject in self.subjects:
            print(f'{self.last_name} does not learn this subject')
            return None
        else:
            if len(self.__study_res[subject]['scores']) > 0:
                res = f'{self.last_name} in {subject} has scores: {self.__study_res[subject]["scores"]}\n' \
                      f'The average score is: {round(mean(self.__study_res[subject]["scores"]), 2)}'
            else:
                res = f'{self.last_name} has no scores in {subject}'
            return res

    def write_test_res(self, subject: str, score: int):
        subject = subject.capitalize()
        if not TEST_MIN <= score <= TEST_MAX or not subject in self.subjects:
            raise ValueError(f'Test result is not between {TEST_MIN} and {TEST_MAX} or subject not in {self.subjects}')
        else:
            self.__study_res[subject]['tests'].append(score)

    def show_test_res_and_avg(self, subject: str):
        subject = subject.capitalize()
        if not subject in self.subjects:
            print(f'{self.last_name} does not learn this subject')
            return None
        else:
            if len(self.__study_res[subject]['tests']) > 0:
                res = f'{self.last_name} in {subject} has test results: {self.__study_res[subject]["tests"]}\n' \
                      f'The average test result is: {round(mean(self.__study_res[subject]["tests"]), 2)}'
            else:
                res = f'{self.last_name} has no test results in {subject}'
            return res

    @property
    def average_score(self):
        all_avgs = []
        for value in self.__study_res.values():
            for key in value.keys():
                if key == 'scores':
                    if len(value[key]) > 0:
                        all_avgs.append(mean(value[key]))
        res = round(mean(all_avgs),2)
        return res

if __name__ == '__main__':
    student = Student('Surdin', 'Vladimir', 'Georgievich')
    print(student)
    print(type(student))
    print(student.subjects)
    print(student.show_score_and_avg('math'))
    print(student.show_score_and_avg('english'))
    student.write_score('math', 5)
    student.write_score('math', 4)
    student.write_score('math', 5)
    student.write_score('english', 5)
    print(student.show_score_and_avg('math'))
    print(student.show_score_and_avg('english'))
    print(student.show_test_res_and_avg('math'))
    student.write_test_res('MATH',89)
    student.write_test_res('MATH', 78)
    student.write_test_res('MATH', 59)
    print(student.show_test_res_and_avg('math'))
    print(student)
    print(student.average_score)