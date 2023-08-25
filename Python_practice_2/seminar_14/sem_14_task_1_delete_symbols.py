# Задание №1
# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_letters

def validate_string(text:str)->str|None:
    res = ''
    if len(text) > 0:
        for sth in text:
            if 65<=ord(sth)<=90 or 97<= ord(sth)<=122 or sth == ' ':
                res = res + sth.lower()
    return res

def sem_validate_string(text: str):
    return (''.join(char for char in text if char in ascii_letters or char == ' ')).lower()

if __name__ == '__main__':
    text = 'pakjsbglwkaefnFYK{OHPUIG5  67@@#!f3'
    print(validate_string(text))
    print(sem_validate_string(text))