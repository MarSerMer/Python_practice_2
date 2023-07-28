# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

"""
This module will let you play "the guess number" game
"""
from random import randint as ri


def guessing(less_border: int, up_border: int, number_of_tries: int)->bool:
    num_to_guess = ri(less_border,up_border)
    count_of_tries = 0
    message = ''
    while count_of_tries < number_of_tries:
        num_from_user = int(input('Please enter the number: '))
        if num_from_user == num_to_guess:
            message = 'You guessed!!!'
            return True
        elif num_from_user > num_to_guess:
            message = 'This number is too big, try again.'
        elif num_from_user < num_to_guess:
            message = 'This number is too small, try again.'
        print(message)
    print("You could not guess, sorry...")
    return False

if __name__ == '__main__':
    print(guessing(1,20,5))
