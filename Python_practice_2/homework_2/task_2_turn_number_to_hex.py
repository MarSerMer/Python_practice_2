# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

DIVIDER: int = 16
def get_number_from_user() -> int:
    info = input("Please enter a number: ")
    while not info.isdigit():
        info = input('Wrong enter. Please enter again: ')
    if int(info) >= 0:
        return int(info)
    else:
        return get_number_from_user()

def convert_to_hexadecimal():
    patient: int = get_number_from_user()
    print(hex(patient))
    res: str = ''
    dictt = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7:'7',\
             8:'8',9:'9',10:'A',11:'B', 12:'C',13:'D', 14:'E',15:'F'}
    while patient > 0:
        div = patient % 16
        res = dictt[div] + res
        patient = patient // 16
    print(res)

convert_to_hexadecimal()
