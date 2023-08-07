# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.


from sem_9_task_2_decorate_guessing import deco_guessing_number as check_numbers
from sem_9_task_3_deco_to_JSON import deco_info_to_json as write_to_json
from sem_9_task_4_launches import deco_launches as repeat

MIN_NUM_GUESS = 1
MAX_NUM_GUESS = 100

MIN_ATTEMPTS = 1
MAX_ATTEMPTS = 10

@repeat(3)
@check_numbers
@write_to_json
def try_to_guess(num_to_guess: int, attempts: int):
    """A simple and funny game. Try to guess the number. Beware, attempts are limited!"""
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
    try_to_guess(101, 13)