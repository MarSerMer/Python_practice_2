# Напишите функцию, которая открывает на чтение созданные в прошлых задачах
# файлы с числами и именами.
# ✔ Перемножьте пары чисел.
# В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

NUMS_FILE = 'file_for_s7_task_1'
NAMES_FILE = 'file_for_s7_task_2_aliases'
RES_FILE = 'file_for_s7_task_3'


def strange_task_3(names_file: str = NAMES_FILE, nums_file: str = NUMS_FILE, res_file: str = RES_FILE):
    with open(nums_file, 'r') as f:
        list_of_nums = list(f)
    with open(names_file, 'r') as f:
        list_of_names = list(f)
    if len(list_of_nums) > len(list_of_names):
        count: int = len(list_of_nums) - len(list_of_names)
        for i in range(0, count):
            list_of_names.append(list_of_names[i])
    if len(list_of_names) > len(list_of_nums):
        count: int = len(list_of_names) - len(list_of_nums)
        for i in range(0, count):
            list_of_nums.append(list_of_nums[i])
    print(list_of_nums)
    print(list_of_names)
    list_to_file: list = []
    for i in range(0, len(list_of_nums)):
        mult = int(list_of_nums[i].split('|')[0]) * float(list_of_nums[i].split('|')[1])
        if mult >= 0:
            list_to_file.append(f'{list_of_names[i][0:-1].upper()} {int(mult)}\n')
        else:
            list_to_file.append(f'{list_of_names[i][0:-1].lower()} {abs(mult)}\n')
    with open(res_file, 'a') as f:
        for pair in list_to_file:
            f.write(pair)


if __name__ == "__main__":
    strange_task_3()
