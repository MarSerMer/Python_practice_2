# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def get_list_of_sorted_unicodes(s: str) -> list[int]:
    symbols: set = set(map(ord,s)) # ord и возвращает код символа из юникода
    result = sorted(list(symbols), reverse=True)
    return result


lst_res = get_list_of_sorted_unicodes('А роза упала на лапу Азора')
print(lst_res, end='  ')

