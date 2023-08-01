# Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
import random

vowels = ['e','y','u','i','o','a']
consonants = ['q','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

def put_aliases_to_file():
    alias: str = generate_alias().capitalize()
    with open('file_for_s7_task_2_aliases', 'a') as f:
        print(alias, file=f)


def generate_alias()->str:
    global vowels
    global consonants
    res_v = random.sample(vowels,3,counts=None)
    res_c = random.sample(consonants,3,counts=None)
    res = res_c + res_v
    random.shuffle(res)
    res_str = (''.join(res))
    return res_str

if __name__ == "__main__":
    put_aliases_to_file()