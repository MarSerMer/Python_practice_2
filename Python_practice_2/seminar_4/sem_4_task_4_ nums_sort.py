# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def sort_numbers(lst: list):
    print('The incoming list: ', lst)
    for i in range (0, len(lst)):
        for j in range (i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    print(lst)



sort_numbers([2, 12, 7 , 43, -5])