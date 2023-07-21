# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

s: str = 'А роза упала на лапу Азора'
# dict_from_string = {l:ord(l) for l in s}
# print(dict_from_string)

res_dict = {}
for l in s:
    res_dict[l] = ord(l)
print(res_dict)

# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили. # Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение, # обращаясь к итератору, а не к словарю.

HOW_MANY_PAIRS_NEEDED = 5

iter_for_dict = iter(res_dict.items())
for _ in range(HOW_MANY_PAIRS_NEEDED):
    print(next(iter_for_dict))
