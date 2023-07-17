# Задание №3
# Погружение в Python | Коллекции
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

def sem_3_task_3():
    data_string: str = input('Please enter some datas: ')
    res = None
    if not data_string.startswith('-') and data_string.isdecimal():
        res = int(data_string)
    elif data_string.replace('.','',1).replace('-','',1).isdecimal() \
            and data_string.count('-') <= 1 \
            and (data_string[1:].count('-') == 0 \
            and data_string.count('.') == 1):
        res = float(data_string)
    else:
        has_upper: bool = False
        for item in data_string: # ищем, есть ли хоть один знак верхнего регистра
            if item.isupper():
                has_upper = True
                break
        if has_upper:
            res = data_string.lower()
        else:
            res = data_string.upper()
    print(res)
    print(type(res))

sem_3_task_3()
