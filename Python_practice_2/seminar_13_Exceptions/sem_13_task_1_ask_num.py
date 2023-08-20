# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

def ask_user_for_num():
    while True:
        data = input('Please enter int or float number: ')
        try:
            num = int(data)
            break
        except ValueError as e:
            # print('This is not int.')
            try:
                num = float(data)
                break
            except ValueError as ve:
                print('This data is not float or int. Please try to enter another data: ')
    return num

print(ask_user_for_num())