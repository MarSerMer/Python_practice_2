# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

"""
Getting information about dates or years
"""

__all__ = ['check_if_date_exists']

def check_if_date_exists(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if day > 31 or day < 1 or month > 12 or month < 1 or year > 9999 or year < 1:
        return False
    elif month!=2 and month in (4,6,9,11) and day>30:
        return False
    elif month == 2 and _check_year_if_leap(year):
        if day>29:
            return False
    elif month == 2 and not _check_year_if_leap(year):
        if day > 28:
            return False
    return True


def _check_year_if_leap(year: int)->bool:
    if year%4 !=0 or (year%100 == 0 and year %400!=0):
        return False
    return True


if __name__ == '__main__':
    s = 'Please enter a date like DD.MM.YYYY and you will find out if such date can exist: '
    print(check_if_date_exists(input(s)))