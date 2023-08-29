# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

from datetime import datetime
import logging

logging.basicConfig(filename='file_for_task_4_dates.log',encoding='utf-8',level=logging.ERROR)
logger = logging.getLogger(__name__)

WEEK_DAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')
MONTHS = ('янв','фев','мар','апр','мая','июн','июл','авг','сен','окт','ноя','дек')

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
    print(text_to_date('1-й четверг ноября'))
    print(text_to_date('3-я среда мая'))
    print(text_to_date('1-й четверг'))
