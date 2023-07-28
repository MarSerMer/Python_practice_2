# Добавьте в модуль с загадками функцию, которая принимает на вход
# строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из
# защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

"""
The Riddle game
Try to guess the riddle. Think well and be fast! The number of tries is limited!
"""

__all__ = ['guess_the_riddle', 'many_riddles', 'show_guess_info']


NUMBER_OF_TRYINGS = 2

_guessing_info: dict = {}

def guess_the_riddle(riddle, answers: list[str], number_of_tryings: int) -> int:
    print(f'Here is the riddle: {riddle} \n You have {NUMBER_OF_TRYINGS} tries to guess it.')
    count_of_tries: int = 1
    while count_of_tries <= number_of_tryings:
        answer_from_user: str = input('Enter your answer: ')
        if answer_from_user in answers:
            return count_of_tries
        count_of_tries += 1
    return 0

def fill_the_guess_info (guess: str, num_of_try: int):
    _guessing_info.update({guess:num_of_try})

def many_riddles(riddles: dict[str:list],number_of_tryings = 3):
    for key, value in riddles.items():
        n = guess_the_riddle(key,value,number_of_tryings)
        fill_the_guess_info(key,n)

def show_guess_info():
    show_info = (f'Загадка {key} отгадана с {n} попытки \n' if n > 0 else f'Загадка {key} не отгадана \n'\
                 for key,n in _guessing_info.items())
    print(*show_info)


if __name__ == '__main__':
    riddles = {
        'Зимой и летом одним цветом': ['Потолок', 'Палка', 'Штаны', 'Словарь', 'Молоко'],
        'Кто-кто в теремочке живет?': ['Мышка', 'Лягушка', 'Арендаторы'],
        'Угадайте число от 1 до 7': ['3','5','7']
    }
    many_riddles(riddles)
    show_guess_info()


