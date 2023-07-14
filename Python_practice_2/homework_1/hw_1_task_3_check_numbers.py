# Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу
# и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MAX_NUMBER = 100000
MIN_NUMBER = 0

def check_number_if_prime():
    number = ask_for_information()
    answer = "Prime"
    for i in range (2, number):
        if number%i == 0:
            answer = 'Not prime'
            break
    print(answer)

def ask_for_information():
    n = input(f'Please enter a number: ')
    while not n.isdigit() or int(n) < MIN_NUMBER or int(n) > MAX_NUMBER:
        n = input('Wrong enter. Please enter again: ')
    return int(n)

check_number_if_prime()