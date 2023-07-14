# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.

BINARY_DIVIDER = 2
OCT_DIVIDER = 8


def get_number_from_user() -> tuple[int, int]:
    info = input("Please enter a number and a divider. Use space between them: ")
    r, d = info.split()
    return int(r), int(d)


def converter(patient: int, divider: int):
    r: str = ''
    while patient > 0:
        r = str(patient % divider) + r
        patient //= divider
    return r


patient, divider = get_number_from_user()
if isinstance(patient, int) and divider in (BINARY_DIVIDER, OCT_DIVIDER):
    print(converter(patient, divider))
else:
    print("Sth went wrong. Try again. ")

print(bin(patient))
print(oct(patient))
print(hex(patient))
