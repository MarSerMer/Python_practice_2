# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import random
import os
from os import path

MIN_NAME_LENGTH = 5
MAX_NAME_LENGTH = 7
MIN_BYTES_TO_FILE = 16
MAX_BYTES_TO_FILE = 112
AMOUNT_OF_FILES = 5
DIRECTORY = 'task_4_files'

vowels = ['e', 'y', 'u', 'i', 'o', 'a']
consonants = ['q', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']


def generate_alias(letters_in_name: int) -> str:
    global vowels
    global consonants
    res = random.sample((vowels + consonants), letters_in_name)
    res_str = (''.join(res))
    return res_str

def check_dir(dir=DIRECTORY,**kwargs)->None:
    if not path.exists(dir):
        os.mkdir(dir)
    os.chdir(dir)
    creating_different_types_of_files(**kwargs)


def create_files(*, file_ext: str = 'txt', \
                 min_name_length: int = MIN_NAME_LENGTH, \
                 max_name_length: int = MAX_NAME_LENGTH, \
                 min_bytes: int = MIN_BYTES_TO_FILE, \
                 max_bytes: int = MAX_BYTES_TO_FILE, \
                 amount_of_files: int = AMOUNT_OF_FILES)->None:
    if min_name_length < MIN_NAME_LENGTH or max_name_length > MAX_NAME_LENGTH \
            or min_bytes < MIN_BYTES_TO_FILE or max_bytes > MAX_BYTES_TO_FILE \
            or amount_of_files <= 0 or amount_of_files > AMOUNT_OF_FILES:
        print('Wrong incoming datas. The files can not be created.')
    else:
        for _ in range(0, amount_of_files):
            name_length = random.randint(min_name_length, max_name_length)
            final_name = f'{generate_alias((name_length))}.{file_ext}'
            bytes_to_file = bytes(random.randint(0,255) for _ in range(0,random.randint(min_bytes, max_bytes)))
            with open(final_name, 'wb') as f:
                f.write(bytes_to_file)

def creating_different_types_of_files(**kwargs)->None:
    for ext, amount in kwargs.items():
        create_files(file_ext=ext,amount_of_files=amount)


if __name__ == "__main__":
    check_dir(txt=2,py=2,jpeg = 2)