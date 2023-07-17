# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

start_list: list = [2, 'a', 3.17, [1, 2], 3, 2, [1, 2], 2.12, 'fire', 'a',7.23, 8, None, None, False, False, True]
print(start_list)
res_list: list = []
for value in start_list:
    print(value, start_list.count(value))
    if start_list.count(value) > 1 and value not in res_list:
        res_list.append(value)
print(res_list)
