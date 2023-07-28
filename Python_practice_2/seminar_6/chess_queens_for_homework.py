# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

from random import randint

"""
This module lets you see if 8 chess queens can beat each other or not
Just give their coordinates and see True or False

"""
__all__ = ['check_queens_if_not_beated','find_options']


# вообще в шахматах используют координаты вида буква+цифра,
# где буква обозначает вертикаль, а цифра - горизонталь
# В задаче просят использовать только цифры,
# и я буду исходить из того, что первая цифра в паре обозначает вертикаль, а вторая - горизонталь



def check_queens_if_not_beated(positions: dict[str:list]) -> bool:
    # вообще изначально функция принимала 8 пар чисел, но при выполнении второго задания я \
    # решила поменять на словарь
    for key in positions.keys():  # проверяем, стоят ли хотя бы 2 ферзя на одной вертикали
        for k in positions.keys():
            if key == k:
                continue
            if positions[key][0] == positions[k][0]:
                return False
    for key in positions.keys():  # проверяем, стоят ли хотя бы 2 ферзя на одной горизонтали
        for k in positions.keys():
            if key == k:
                continue
            if positions[key][1] == positions[k][1]:
                return False
    # если всё еще не бьют друг друга, нужно проверить диагонали:
    for key in positions.keys():
        for k in positions.keys():
            if k == key:
                continue
            if positions[key][0] > positions[k][0] and positions[key][0] - positions[k][0] == positions[key][1] - \
                    positions[k][1]:
                return False
    return True


def random_positions(positions=None) -> dict[str:list]:
    print('Random pos started')
    if positions == None:
        positions: dict = {}
        for i in range(1, 9):
            positions[f'q{i}'] = [randint(1,8),randint(1,8)]
    else:
        for i in range(1, 9):
            positions[f'q{i}'] = [randint(1,8),randint(1,8)]
    return positions


def find_options(number_of_options=4) -> dict[str:list] | None:
    count = 0
    positions = None
    result: dict = {}
    while count < number_of_options:
        positions = random_positions(positions)
        if check_queens_if_not_beated(positions):
            count += 1
            result[f'Option {count}: '] = positions
    return result


if __name__ == '__main__':
    find_options(2)
