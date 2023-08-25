# Задание №2
# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

def validate_string(text:str)->str|None:
    """
    This function takes a string and leaves latin letters or spaces.
    All other symbol are deleted from the incoming string.
    The result is given in lowercase.
    >>> validate_string('ff ll h')
    'ff ll h'
    >>> validate_string('FF LL h')
    'ff ll h'
    >>> validate_string('FF LL, -:h')
    'ff ll h'
    >>> validate_string('ff ll hГеннадий')
    'ff ll h'
    >>> validate_string('ff ll -:hГеннадий')
    'ff ll h'
    """
    res = ''
    if len(text) > 0:
        for sth in text:
            if 65<=ord(sth)<=90 or 97<= ord(sth)<=122 or sth == ' ':
                res = res + sth.lower()
    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
