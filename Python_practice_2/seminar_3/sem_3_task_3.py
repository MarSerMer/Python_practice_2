# Задание №3
# Погружение в Python | Коллекции
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

manual_list = (2, 'a', 3.17, [1, 2], 3, [1, 7], 2.12, 'fire', 7.23, 8, None, False, True)
print(type(manual_list))
res_dict = {}
print(type(res_dict))
print('The for starts')
# for item in manual_list:
#     if type(item) in res_dict.keys():
#         res_dict[type(item)].append(item)
#     else:
#         res_dict[type(item)] = [item]
for item in manual_list:
    key = res_dict.setdefault(type(item),list())
    key.append(item)

print('Final print:')
print(res_dict)
