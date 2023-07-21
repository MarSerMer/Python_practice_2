# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

import decimal

names: list = ['Jake', 'Smith', 'van Rossum']
salaries: list = [1500, 2560, 10560]
bonuses: list = ['15%', '23%', '45%']
def get_bonus(salaries: list, bonuses:list) -> list[decimal.Decimal]:
    res_bonuses = []
    for salary, bonus in zip(salaries,bonuses):
        res_bonuses.append(salary * decimal.Decimal(bonus[:-1]) / 100)
    return res_bonuses

print(get_bonus(salaries,bonuses))

dict_gen = {name:res for name,res in zip(names,get_bonus(salaries,bonuses))}
print(*dict_gen.items())