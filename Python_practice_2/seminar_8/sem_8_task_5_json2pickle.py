# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import os
import json
import pickle

DIR = 'files_for_task_5'

def find_json_ant_turn_2_pickle(dir:str=DIR)->None:
    lst_of_json = filter(lambda f: f[-5:] == '.json',os.listdir(dir))
    os.chdir(dir)
    for j_file in lst_of_json:
        with open (j_file, 'r', encoding='utf-8') as jf:
            data = json.load(jf)
        with open(f'{j_file[:-5]}.pickle', 'wb') as pw:
            pickle.dump(data,pw)

find_json_ant_turn_2_pickle('.')

