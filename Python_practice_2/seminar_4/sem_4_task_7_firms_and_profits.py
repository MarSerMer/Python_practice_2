# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

def find_out_if_all_profitable(dict: dict[str:list[int|float]]) -> bool:
    for names in dict.keys():
        dict[names] = float(sum(dict[names]))

    return all(map(lambda value:value > 0, dict.values()))
    # return all(map(lambda: x:sum(x) > 0, dict.values())  - можно вот так, т.е. получить сумму сразу в строке

dict_of_firms = {'Рога и копыта': [-5, -10, -15, 500],\
                 'Spam': [2,3,7,18.55,-1],\
                 'Eggs': [7,0,75,85,4,2,1,0]}

print(find_out_if_all_profitable(dict_of_firms))