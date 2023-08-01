# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from sem_7_task_4_create_files import create_files

MIN_NAME_LENGTH = 5
MAX_NAME_LENGTH = 7
MIN_BYTES_TO_FILE = 16
MAX_BYTES_TO_FILE = 112
AMOUNT_OF_FILES = 5

def creating_different_types_of_files(**kwargs)->None:
    for ext, amount in kwargs.items():
        create_files(file_ext=ext,amount_of_files=amount)

if __name__ == "__main__":
    # dict_ = {'txt':2, 'py':2}
    creating_different_types_of_files(txt=2,py=2)
