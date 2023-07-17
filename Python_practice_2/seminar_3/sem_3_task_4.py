# Задание №4
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

HOW_MANY_REPEATS = 2
manual_list = [2, 'a', 3.17, [1, 2], 3, [1, 7], 3.17, 'fire', 'a', 7.23, 3.17, 3.17,  8, None,[1,2], False, True, None]
print(manual_list)
items_of_2 = []
for item in manual_list:
    print(manual_list.count(item))
    if manual_list.count(item) == HOW_MANY_REPEATS:
        items_of_2.append(item)
print(items_of_2)

for val in items_of_2:
    manual_list.remove(val)
print(manual_list)