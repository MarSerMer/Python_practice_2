# Задание №5
# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить.
# В этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые, т.е не мая, а 5.

from datetime import datetime
import logging
import argparse

logging.basicConfig(filename='file_for_task_5_dates.log',encoding='utf-8',level=logging.ERROR)
logger = logging.getLogger(__name__)

WEEK_DAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')
MONTHS = ('янв','фев','мар','апр','мая','июн','июл','авг','сен','окт','ноя','дек')

def parse():
    weekday = datetime.now().weekday
    month = datetime.now().month
    parser = argparse.ArgumentParser (prog='date from string',
                                      description='put a string and get a data',
                                      epilog='get_data(“1-й четверг ноября”)')
    parser.add_argument('-c','--count',default=1,help='number of weekday in month, like "third monday"')
    parser.add_argument('-w', '--weekday', default=weekday, help='name of weekday')
    parser.add_argument('-m', '--month', default=month, help='name of month')
    args = parser.parse_args()
    return text_to_date(f'{args.count} {args.weekday} {args.month}')
def text_to_date(text: str)->datetime | None:
    try:
        count, weekday, month = text.split()
    except ValueError as e:
        logger.error(f'{e}: \n{text} is impossible to be split on three parts!')
        return None
    count = int(count[0])
    weekday = WEEK_DAYS.index(weekday[:3])
    month = MONTHS.index(month[:3]) + 1
    i = 0
    for day in range(1,32):
        date = datetime(day=day,month=month,year=datetime.now().year)
        if date.weekday() == weekday:
            i += 1
            if i == count:
                return date

if __name__ == '__main__':
    print(parse())