# В модуль с проверкой даты добавьте возможность запуска в терминале
# с передачей даты на проверку.

"""
Getting information about dates or years
Now using terminal available
"""

from sys import argv

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
    print('So you entered a date like DD.MM.YYYY, so you can get information if such date can exist: ')
    s = argv[1]
    print(check_if_date_exists(s))