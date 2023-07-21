# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

dogs = 'corgies'
cats = 7.02
s = 'just s'
lori = ['lori','list']
kapibara = True
forks = 2

def strange_task_with_s() -> None:
    global_vars = globals()
    res_dict = {}
    for key, value in global_vars.items():
        if key == 's':
            continue
        if key.endswith('s'):
            res_dict[key[:-1]] = value
            global_vars[key] = None
    for key,value in res_dict.items():
        global_vars[key] = value


strange_task_with_s()
print(globals())