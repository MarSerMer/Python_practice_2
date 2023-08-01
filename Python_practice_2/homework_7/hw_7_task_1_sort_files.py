# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
from os import path
from pathlib import Path



DICT_OF_EXTS = {'text_files':['txt','doc'],
                'photos':['jpeg','bmp'],
                'programs':['py','html'],
                'videos':['mp4','mkv'],
                'audio':['mp3']}

def check_dir(dir)->None:
    if not path.exists(dir):
        os.mkdir(dir)


def sort_files(dirs_and_exts:dict [str:list])->None:
    list_of_f = os.listdir()
    for dir in dirs_and_exts.keys():
        check_dir(dir)
        for end in dirs_and_exts[dir]:
            for f in list_of_f:
                if f.endswith(end):
                    o_f = Path(f)
                    n_f = o_f.replace(Path.cwd()/dir/o_f)
                    # os.replace(f,dir) - вот это вот выдавало ошибку доступа :(


if __name__ == "__main__":
    os.chdir(r'C:\Users\User\Desktop\Geek Brains\16 Погружение в PYTHON\Python_practice_2\homework_7\task_1_files')
    sort_files(DICT_OF_EXTS)
