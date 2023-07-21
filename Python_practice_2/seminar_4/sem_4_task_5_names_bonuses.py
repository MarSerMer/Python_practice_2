# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

import decimal
def get_names_ans_bonuses(names: list[str], salaries: list[int], bonuses:list[str]) -> dict [str:decimal.Decimal]:
    names_and_bonuses: dict = {}
    for name, salary, bonus in zip(names, salaries, bonuses):
        names_and_bonuses[name] = salary * decimal.Decimal(bonus[:-1]) / 100
    return names_and_bonuses


names: list = ['Jake', 'Smith', 'van Rossum']
salaries: list = [1500, 2560, 10560]
bonuses: list = ['15%', '23%', '45%']

print(get_names_ans_bonuses(names,salaries,bonuses))