# Задание №1
# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

def task_1_part_1():
    task_1_list = [1,2,3,7,6,3,4,5,2,8,1,9,1,2]
    set_res = list(set(task_1_list))
    print(set_res)
    print(type(set_res))

task_1_part_1()
def task_1_part_2():
    task_1_list = [1, 2, 3, 7, 6, 3, 4, 5, 2, 8, 1, 9, 1, 2]
    res_list = []
    for item in task_1_list:
        if item not in res_list:
            res_list.append(item)
    print(task_1_list)
    print(res_list)

task_1_part_2()