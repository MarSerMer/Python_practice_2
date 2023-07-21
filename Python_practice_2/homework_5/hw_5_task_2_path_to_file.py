# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def cut_the_path(s: str) -> tuple[str]:
    *path, name_and_way = s.split("/")
    path = ','.join(path).replace(',','/')
    name, way = name_and_way.split('.')
    res_tuple = (path,name,way)
    return res_tuple



path: str = "C:/Users/User/Desktop/Geek Brains/16 Погружение в PYTHON/Python_practice_2/string.txt"
print(cut_the_path(path))