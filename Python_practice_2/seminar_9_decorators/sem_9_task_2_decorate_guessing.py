# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from typing import Callable
from random import randint
from functools import wraps

MIN_NUM_GUESS = 1
MAX_NUM_GUESS = 100

MIN_ATTEMPTS = 1
MAX_ATTEMPTS = 10

def check_nums(num_to_check, min_num, max_num)->bool:
    return min_num<=num_to_check<=max_num

def deco_guessing_number(func: Callable) -> Callable[[int,int], None]:
    @wraps(func)
    def wrapper(num_to_guess: int, attempts: int, *args, **kwargs):
        if not check_nums(num_to_guess,MIN_NUM_GUESS,MAX_NUM_GUESS):
            print('Changing number to random.')
            num_to_guess = randint(MIN_NUM_GUESS,MAX_NUM_GUESS)
        if not check_nums(attempts,MIN_ATTEMPTS,MAX_ATTEMPTS):
            print('Changing attempts to random.')
            attempts = randint(MIN_ATTEMPTS,MAX_ATTEMPTS)
        return func(num_to_guess, attempts)
    return wrapper


@deco_guessing_number
def try_to_guess(num_to_guess: int, attempts: int):
    print(f'Try to guess the number! \n'
          f'It is from {MIN_NUM_GUESS} to {MAX_NUM_GUESS}. \n '
          f'You will have {attempts} attempts: ')
    count = 0
    while count < attempts:
        user_num = int(input())
        if user_num == num_to_guess:
            print("YOU GUESSED!!! CONGRATULATIONS!")
            break
        else:
            count += 1
            print(f'No, you were wrong. You have {attempts - count} attempts left. ')
            if attempts > count:
                print("Try again: ")
                if user_num > num_to_guess:
                    print('Your number was too big.')
                else:
                    print('Your number was too small.')
    print('Game over.')


if __name__ == '__main__':
    try_to_guess(101, 3)

