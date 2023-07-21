# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import decimal
import colorama
from colorama import Fore, Back, Style
colorama.init()

START_SUM: int = 0
MULTIPLICITY: int = 50
PERSENTAGE_FOR_WITHDRAWAL: float = 0.015
MIN_FEE: int = 30
MAX_FEE: int = 600
COUNT_OF_TW_OPERATIONS: int = 3
PERSENTAGE_AFTER_TW_OPERATIONS: float = 0.03
SUM_FOR_WEALTH_TAX: int = 5_000_000
WEALTH_TAX: float = 0.1
total_sum: decimal.Decimal = decimal.Decimal(START_SUM)

# operations = ['top_up', 'withdraw', 'exit', 'information', 'account information']
operations = ['T', 'W', 'E', 'I', 'AI']
welcome_text: str = 'Welcome to the ATM. \n Please choose the operation you want to perform. \n' \
                    'Enter T to top up your account. \n' \
                    'Enter W to withdraw money. \n' \
                    'Enter I to get information about how this ATM works.\n' \
                    'Enter E to exit.\n'

def ask_for_sum(s) -> int:
    # проверить как работает! нужно не дать ввести не число и не дать ввести отрицательное
    # Сумма пополнения и снятия кратны 50 у.е.
    res_sum = input(Fore.WHITE + s)
    if res_sum.isdigit():
        if int(res_sum) < 0 or int(res_sum) % 50 != 0:
            return ask_for_sum(Fore.WHITE + 'Wrong sum. Please enter again: ')
        else:
            return int(res_sum)
    else:
        return ask_for_sum(Fore.WHITE + 'Not digital. Please enter again: ')

def check_for_withdraw(total_sum, sum_for_withdraw):
    if sum_for_withdraw * PERSENTAGE_FOR_WITHDRAWAL < MIN_FEE:
        if (sum_for_withdraw + MIN_FEE) <= total_sum:
            total_sum = total_sum - sum_for_withdraw - MIN_FEE
        else:
            print("Insufficient funds in the account. The withdraw can not be done.")
    elif sum_for_withdraw * PERSENTAGE_FOR_WITHDRAWAL > MAX_FEE:
        if (sum_for_withdraw + MAX_FEE) <= total_sum:
            total_sum = total_sum - sum_for_withdraw - MAX_FEE
    elif (sum_for_withdraw + sum_for_withdraw * PERSENTAGE_FOR_WITHDRAWAL) <= total_sum:
        total_sum = total_sum - sum_for_withdraw * (1 + PERSENTAGE_FOR_WITHDRAWAL)
    return total_sum

def check_if_time_for_profit(count_of_operations, total_sum):
    if count_of_operations == COUNT_OF_TW_OPERATIONS:
        total_sum = round(total_sum + total_sum * decimal.Decimal(PERSENTAGE_AFTER_TW_OPERATIONS),2)
        count_of_operations = 0
        print(Fore.BLUE + 'Profit added')
    return count_of_operations, total_sum


def check_if_too_rich(total_sum) -> decimal.Decimal:
    # При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
    # операцией, даже ошибочной
    if total_sum > SUM_FOR_WEALTH_TAX:
        total_sum = total_sum * (1 - WEALTH_TAX)
        print(Fore.RED + 'Rich tax is taken')
        print(Fore.RED + 'Now you have ', total_sum)
    return total_sum


def top_up(total_sum: decimal.Decimal) -> decimal.Decimal:
    top_up_sum = int(ask_for_sum('What sum do you want to add? '))
    total_sum = total_sum + decimal.Decimal(top_up_sum)
    in_and_out_list.append(f'{top_up_sum} added')
    return total_sum

in_and_out_list: list = []
count_of_operations: int = 0
while True:
    print()
    operation = str.upper(input(Fore.YELLOW + welcome_text))
    match operation:
        case 'T':  # хотят пополнить
            print(Fore.GREEN + "Now you have: ", total_sum)
            total_sum = check_if_too_rich(total_sum)
            total_sum = top_up(total_sum)
            count_of_operations += 1
            count_of_operations, total_sum = check_if_time_for_profit(count_of_operations, total_sum)
            print(Fore.BLUE + "Now you have: ", total_sum)
        case 'W':  # хотят снять
            # Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
            print(Fore.GREEN + "Now you have: ", total_sum)
            total_sum = check_if_too_rich(total_sum)
            if total_sum < MULTIPLICITY + MIN_FEE:
                print("There is less than 80 on your amount. You can't withdraw anything.")
                continue
            else:
                sum_for_withdraw = ask_for_sum('What sum do you want to withdraw? ')
                temp: decimal.Decimal = total_sum
                total_sum = check_for_withdraw(total_sum, sum_for_withdraw)
                if temp != total_sum:
                    count_of_operations += 1
                    in_and_out_list.append(f'{sum_for_withdraw} was taken')
                count_of_operations, total_sum = check_if_time_for_profit(count_of_operations, total_sum)
            print(Fore.BLUE + "Now you have: ", total_sum)
        case 'E':
            print(Fore.GREEN + "Now you have: ", total_sum)
            print('The program will be closed.')
            break
        case 'I':
            print('You asked for information about how this ATM works.\n' \
                  'You can top up or withdraw money from your account. \n'
                  'Th sum of any operation should be multiple of 50. \n'
                  'For the withdrawal  ATM will take 1,5% of the withdrawed sum (but not less 30 and not over 600). \n'
                  'You can’t take more money than you have on your account. \n'
                  'After every three top up or withdraw operations the ATM will add 3% to your account. \n'
                  'Please be informed that if your account has more than 5 000 000 on it, \n '
                  'the ATM will take 10% from it before every operation! \n')
        case 'AI':
            for i in in_and_out_list:
                print(Fore.WHITE + i)
        case _:
            print('Unknown command.')