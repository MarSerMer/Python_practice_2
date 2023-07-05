# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

def task_5():
    n = int(input("Enter n: "))
    i = 1
    e = int(input("Enter e: "))
    result = 0

    while i < n:
        if i % e == 0 or i % 2:
            i += 1
            continue
        else:
            result += i
        i += 1

    print(result)

task_5()

# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

def task_6():
    GREGORIAN_START = 1582
    SMALL_DIVIDE = 4
    MIDDLE_DIVIDE = 100
    BIG_DIVIDE = 400
    y = int(input("Enter a year: "))
    result = None
    if y>= GREGORIAN_START:
        if y%SMALL_DIVIDE != 0 or (y%MIDDLE_DIVIDE == 0 and y%BIG_DIVIDE != 0):
            result = 'NO'
        else:
            result = "YES"
    else:
        result = "YEAR BEFORE THE GREGORIAN CALENDAR STARTED"
    print (result)

# task_6()

# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

def task_7():

    LOWER_BORDER = 0
    UPPER_BORDER = 1000
    MB_1 = 10
    MB_2 = 100
    result_text = None
    result_num = None
    num = int(input("Please enter a number: "))
    while num <= LOWER_BORDER or num >= UPPER_BORDER:
        num = int(input("Please enter a number over 0 and less than 1000: "))
    if num < MB_1:
        result_text = "Цифра "
        result_num = num**2
    elif num>=MB_1 and num < MB_2:
        result_text = "Двузначное число "
        result_num = num%10 * num//10
    elif num >= MB_2 and num<UPPER_BORDER:
        result_text = "Трехзначное число"
        result_num = num//100 + ((num%100)//10)*10 + num%10*100

    print(result_text, ' ', result_num)

# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.

def task_8():
    rows = int(input("Сколько рядов у ёлки? "))
    while rows<=0 or rows>10:
        rows = int(input("Неверное количество рядов, введите число от 1 до 10: "))
    for i in range (1, rows+1):
        space_before_star = ' '
        space_for_print = space_before_star * (rows - i)
        star = '*'
        stars_for_print = star*i
        print (space_for_print, stars_for_print)

# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

def task_9():
    for i in range (2, 11):
        for j in range (2, 11):
            print (i, ' * ', j, ' = ', i*j)
        print(' ')

# task_9()