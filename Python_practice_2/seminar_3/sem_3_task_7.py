# Задание №7
# Погружение в Python | Коллекции
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

start_string: str = input('Please enter some string: ')

res_dict = {}

for letter in start_string:
    if letter.isalpha():
        key = res_dict.setdefault(letter, 0)
        res_dict[letter] += 1
print (res_dict)

res_dict_count = {}
for letter in set(start_string):
    # res_dict_count[letter] = start_string.count(letter)
    if letter.isalpha():
        res_dict_count[letter] = start_string.count(letter)
print(res_dict_count)