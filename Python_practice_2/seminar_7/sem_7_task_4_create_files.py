# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import random

MIN_NAME_LENGTH = 6
MAX_NAME_LENGTH = 30
MIN_BYTES_TO_FILE = 256
MAX_BYTES_TO_FILE = 4096
AMOUNT_OF_FILES = 42

vowels = ['e', 'y', 'u', 'i', 'o', 'a']
consonants = ['q', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']


def generate_alias(letters_in_name: int) -> str:
    global vowels
    global consonants
    res = random.sample((vowels + consonants), letters_in_name)
    res_str = (''.join(res))
    return res_str


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
            name = f'task_4_files\{generate_alias(name_length)}.{file_ext}'
            bytes_to_file = bytes(random.randint(0,255) for _ in range(0,random.randint(min_bytes, max_bytes)))
            # bytes_to_file = gr(random.randint(min_bytes, max_bytes))
            with open(name, 'wb') as f:
                f.write(bytes_to_file)


if __name__ == "__main__":
    create_files(file_ext='txt',min_name_length=7,max_name_length=12,max_bytes=300,amount_of_files=2)