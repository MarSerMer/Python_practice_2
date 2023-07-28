# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте
# генераторное выражение.

"""
This module will let you play "the guess number" game
But here you will be able to use terminal to communicate with the game
"""
from random import randint as ri
from sys import argv

__all__ = ['guessing']

def guessing(less_border: int, up_border: int, number_of_tries: int)->bool:
    num_to_guess = ri(less_border,up_border)
    count_of_tries = 0
    message = ''
    while count_of_tries < number_of_tries:
        num_from_user = int(input('Please enter the number: '))
        #num_from_user = int(argv[1])
        if num_from_user == num_to_guess:
            print('You guessed!!!')
            return True
        elif num_from_user > num_to_guess:
            message = 'This number is too big, try again.'
        elif num_from_user < num_to_guess:
            message = 'This number is too small, try again.'
        print(message)
    print("You could not guess, sorry...")
    return False

if __name__ == '__main__':
    nums = (num for num in argv[1:])
    print(guessing(*(int(num) for num in nums)))
    # name, *params = argv
    # print(guessing(*(int(num) for num in params)))

