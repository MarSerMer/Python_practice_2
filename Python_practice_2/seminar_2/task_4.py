# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import math
import decimal

decimal.getcontext().prec = 42
PI: decimal.Decimal = decimal.Decimal(math.pi)


def get_number_from_user() -> decimal.Decimal:
    diameter = input("Please enter a D (over 0 and less than 1000: ")
    return decimal.Decimal(diameter)


d = get_number_from_user()
print(d)
result_length: decimal.Decimal = d * PI
square: decimal.Decimal = (d / 2) ** 2 * PI

print(result_length)
print(square)