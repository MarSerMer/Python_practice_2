# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

"""
The Riddle game
Try to guess the riddle. Think well and be fast! The number of tries is limited!
"""


NUMBER_OF_TRYINGS = 2

def guess_the_riddle(riddle, answers: list[str], number_of_tryings: int) -> int:
    print(f'Here is the riddle: {riddle} \n You have {NUMBER_OF_TRYINGS} tries to guess it.')
    count_of_tries: int = 1
    while count_of_tries <= number_of_tryings:
        answer_from_user: str = input('Enter your answer: ')
        if answer_from_user in answers:
            return count_of_tries
        count_of_tries += 1
    return 0

def many_riddles(riddles: dict[str:list], number_of_tryings = 3):
    for key, value in riddles.items():
        print(guess_the_riddle(key,value,number_of_tryings))

if __name__ == '__main__':
    riddles  = {
        'Зимой и летом одним цветом': ['Потолок', 'Палка', 'Штаны', 'Словарь', 'Молоко'],
        'Кто-кто в теремочке живет?' : ['Мышка','Лягушка','Арендаторы']
    }
    many_riddles(riddles)