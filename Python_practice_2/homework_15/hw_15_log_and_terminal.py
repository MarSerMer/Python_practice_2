# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import logging
from typing import Callable
import argparse

FORMAT = ("{asctime} - {levelname}: \n{msg}")
logging.basicConfig(filename='hw_15_check_date.log',
                    encoding='utf-8',
                    level=logging.NOTSET)
logger = logging.getLogger(__name__)

def parse():
    parser = argparse.ArgumentParser(description='Enter a date dd.mm.yyyy to check if such date exists',
                                     epilog='It is important to enter a right format of the date.')
    parser.add_argument('-d','--date',default='00.00.0000',help='Enter a date dd.mm.yyyy')
    args = parser.parse_args()
    return check_if_date_exists(args.date)
def log_args_and_res(func: Callable):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        dict_to_log = {'args':args,
                **kwargs,
                'result"':res}
        logger.info(dict_to_log)
        return res
    return wrapper

@log_args_and_res
def check_if_date_exists(date: str) -> bool:
    try:
        day, month, year = map(int, date.split('.'))
    except ValueError as e:
        logger.error(f'Внимание! Какая-то ерунда с введенной датой! Я ТАКОЕ сплитануть не могу!\n{e}')
    else:
        if day > 31 or day < 1 or month > 12 or month < 1 or year > 9999 or year < 1:
            return False
        elif month != 2 and month in (4, 6, 9, 11) and day > 30:
            return False
        elif month == 2 and _check_year_if_leap(year):
            if day > 29:
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
    print(parse())