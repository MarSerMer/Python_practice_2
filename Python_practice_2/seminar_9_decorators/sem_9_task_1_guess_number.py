# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from typing import Callable

MIN_NUM_GUESS = 1
MAX_NUM_GUESS = 100

MIN_ATTEMPTS = 1
MAX_ATTEMPTS = 10


def ask_info_to_guess_number()-> Callable[[],None]:
    num_to_guess = int(input(f'Please enter number from {MIN_NUM_GUESS} to {MAX_NUM_GUESS}: '))
    attempts = int(input(f'Please enter number from {MIN_ATTEMPTS} to {MAX_ATTEMPTS}: '))
    def try_to_guess():
        nonlocal num_to_guess
        nonlocal attempts
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
                print(f'No, you were wrong. You have {attempts-count} attempts left. ')
                if attempts > count:
                    print("Try again: ")
                    if user_num > num_to_guess:
                        print('Your number was too big.')
                    else:
                        print('Your number was too small.')
        print('Game over.')
    return try_to_guess


if __name__ == '__main__':
    guess_game = ask_info_to_guess_number()
    guess_game()