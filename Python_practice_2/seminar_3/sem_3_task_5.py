# Задание №5
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

task_5_list = [1,2,3,7,6,3,4,5,2,8,1,9,1,2]
list_of_numbers = []
count = 0
for nums in task_5_list:
    if nums%2:
        print(nums, end = ' ')
        list_of_numbers.append(task_5_list.index(nums,count)+1)
    count += 1

print(' ')
print(list_of_numbers)

list_of_numbers_2 = []
for i, value in enumerate(task_5_list, start=1):
    if value % 2 == 1:
        list_of_numbers_2.append(i)

print(list_of_numbers_2)