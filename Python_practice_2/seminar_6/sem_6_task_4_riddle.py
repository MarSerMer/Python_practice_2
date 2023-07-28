# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

"""
The Riddle game
Try to guess the riddle. Think well and be fast! The number of tries is limited!
"""

NUMBER_OF_TRYINGS = 2


# riddle: str = ''
# list_of_answers: list = []

def guess_the_riddle(riddle, answers: list[str], number_of_tryings: int) -> int:
    print(f'Here is the riddle: {riddle} \n You have {NUMBER_OF_TRYINGS} tries to guess it.')
    count_of_tries: int = 1
    while count_of_tries <= number_of_tryings:
        answer_from_user: str = input('Enter your answer: ')
        if answer_from_user in answers:
            return count_of_tries
        count_of_tries += 1
    return 0


if __name__ == '__main__':
    riddle: str = 'Зимой и летом одним цветом'
    list_of_answers: list = ['Потолок', 'Палка', 'Штаны', 'Словарь', 'Молоко']

    print(guess_the_riddle(riddle, list_of_answers, NUMBER_OF_TRYINGS))
