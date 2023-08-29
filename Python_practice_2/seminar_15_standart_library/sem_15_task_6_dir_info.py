# Задание №6
# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import logging
import argparse
from pathlib import Path
import os
from collections import namedtuple

logging.basicConfig(filename='file_for_task_6-2_dir_info.log', encoding='utf-8',level=logging.INFO)
logger = logging.getLogger(__name__)

File = namedtuple('File', 'filename,extension,is_dir,parent_dir')

def parse_for_dir_info():
    parser = argparse.ArgumentParser(description='Enter path to directory to get information about it.')
    parser.add_argument('-p','--path', default=Path.cwd(), help='Just enter the way to directory')
    args = parser.parse_args()
    return dir_info(args.path)
def dir_info(dir_path: Path):
    for file in dir_path.iterdir():
        f = File(file.stem if file.is_file else file.name,file.suffix,file.is_dir(),file.parent)
        logger.info(f)
        if f.is_dir:
            dir_info(Path(f.parent_dir)/f.filename)

if __name__ == '__main__':
    # print(dir_info(Path(r'C:\Users\User\Desktop\Geek Brains\16 Погружение в PYTHON\Python_practice_2\seminar_15_standart_library')))
    print(parse_for_dir_info())
