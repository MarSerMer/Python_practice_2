# мою версию выполнения задания см. в файле sem_7_task_3
# а тут версия, сделанная на семинаре
# хорошая, вкусная, на неё полезно ориентироваться
# Напишите функцию, которая открывает на чтение созданные в прошлых задачах
# # файлы с числами и именами.
# # ✔ Перемножьте пары чисел.
# # В новый файл сохраните имя и произведение:
# # ✔ если результат умножения отрицательный, сохраните имя
# # записанное строчными буквами и произведение по модулю
# # ✔ если результат умножения положительный, сохраните имя
# # прописными буквами и произведение округлённое до целого.
# # ✔ В результирующем файле должно быть столько же строк,
# # сколько в более длинном файле.
# # ✔ При достижении конца более короткого файла,
# # возвращайтесь в его начало.

import typing as TextIO


def writefile():
    pass


def readline_or_begin(file : TextIO ) -> str:
    text = file.readline()
    if text == "" :
        file.seek(0)
    text = file.readline()
    return text[:-1]

def read_file():
    with (
    open("numbers.txt", encoding="utf-8",) as num_file,
    open("names.txt", encoding="utf-8") as names_file,
    open("result.txt" , 'w' ,encoding="utf-8") as res_file
    ):
        len_names = len(names_file.readlines())
        len_num = len(num_file.readlines())
        for _ in range(max(len_num,len_names)) :
            curr_name = readline_or_begin(names_file)
            curr_nums = readline_or_begin(num_file)
            a,b = curr_nums.split("|")
            math = int(a)*float(b)
            if math > 0 :
                res_file.write( curr_name.upper() + "|" + str(round(math)) + '\n')
            else:
                res_file.write( curr_name.lower() + "|" + str(-math) + '\n')


if __name__ == "__main__":
    read_file()