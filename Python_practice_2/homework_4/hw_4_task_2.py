# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def get_dict_from_keys(**kwargs) -> dict:
    res_dict = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            res_dict[value] = key
        except TypeError:
            value = str(value)
            res_dict[value] = key
    return res_dict

d = get_dict_from_keys(a=3,g=7,h=False)
print(d)
