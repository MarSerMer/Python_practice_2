# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def get_dict_unicode_chars(s: str) -> dict[str:int]:
    num_1, num_2 = map(int, s.split())
    dict = {}
    for i in range(min(num_1,num_2), max(num_1,num_2)+1):
        dict[chr(i)] = i
    return dict


d = get_dict_unicode_chars('54 100')
print(d)