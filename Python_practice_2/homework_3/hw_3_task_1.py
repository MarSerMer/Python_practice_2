# Задание №8
# Погружение в Python | Коллекции
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции  с множествами.
# Код должен расширяться на любое большее количество друзей.

names_and_things = {\
    'Василий': ('Топор', 'Котелок', 'Коврик', 'Спички', 'Аптечка'),\
    'Михаил': ('Коврик', 'Спички', 'Бинокль', 'Спальник','Фотоаппарат','Плащ','Лопатка','Ложки'),\
    'Алексей': ('Коврик','Спички','Спальник','Сухарики','Фотоаппарат'),\
    'Игорь': ('Коврик','Спички','Спальник'),\
    'Фёдор': ('Коврик','Спальник','Соль','Плащ','Палатка','Лопатка')
    }

def find_common (incoming_dict: dict) -> set:
    name_of_tourist: str = None
    for name in incoming_dict.keys():
        name_of_tourist = name
        break
    res_set = set(incoming_dict[name_of_tourist])
    for things in incoming_dict.values():
        res_set = res_set.intersection(set(things))
    return res_set

set_of_common_things = find_common(names_and_things)
print('Things which all tourists have: ', set_of_common_things)

def find_unique (incoming_dict: dict) -> dict:
    res_dict: dict = {}
    for names in incoming_dict.keys():
        check_set = set(incoming_dict[names])
        for n in incoming_dict.keys():
            if n == names:
                continue
            check_set = check_set.difference(set(incoming_dict[n]))
        if len(check_set) != 0:
            res_dict[names] = check_set
    return res_dict

unique_dict = find_unique(names_and_things)
print('These tourists have unique things:',unique_dict)

def strange_task(incoming_dict: dict) -> dict:
    res_dict: dict = {}
    all_things: set = set()
    for things in incoming_dict.values(): # получаем список вообще всех вещей у всех
        all_things = all_things.union(set(things))
    target_things = []
    for thing in all_things: # получаем список вещей, которых нет только у кого-то одного
        count: int = 0
        for individual_lists_of_things in incoming_dict.values():
            if thing in individual_lists_of_things:
                count +=1
        if count == len(incoming_dict) - 1:
            target_things.append(thing)
    for target in target_things:
        for names in incoming_dict.keys():
            if target not in incoming_dict[names]:
                res_dict[target] = f'- эту вещь не взял {names}'
    return res_dict



strange_dict = strange_task(names_and_things)
print(strange_dict)