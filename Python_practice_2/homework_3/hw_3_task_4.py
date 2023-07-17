# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите, какие вещи влезут в рюкзак, передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
#
# *Верните все возможные варианты комплектации рюкзака.

start_dict: dict = {\
    'Котелок': 2, 'Топор':4, 'Палатка':3,\
    'Коврик':0.7, 'Спальник':1.5, 'Спички':0.01,\
    'Аптечка':1.3, 'Дождевик':0.2, 'Консервы':3.7,\
    'Шоколадки':2.2,'Запасная одежда':3.3, 'Миска':0.15,\
    'Крем от комаров':0.2, 'Доширак':2.0,'Нож':0.4,\
    'Резиновые сапоги':0.6,'Орешки':0.9,'Флиска':0.2,\
    'Карты':0.1,'Фляжка':0.8,'Весло':3,\
    'Фонарик':0.2,'Лопатка':0.4,'Спасжилет':1.6,\
    'Пластырь':0.1,'Бинокль':0.4,'Сигнальная ракета':0.9,\
    'Аккумулятор':2.6,'Навес':2.3,'Решетка под котелок':3.5,}

MAX_WEIGHT = 9

def what_to_take(things: dict, max_weight:int = MAX_WEIGHT) -> list:
    list_of_things: list = []
    common_weight: float = 0
    for items in things.keys():
        if common_weight + things[items] > max_weight:
            continue
        list_of_things.append(items)
        common_weight += things[items]
    print(common_weight)
    # print(list_of_things)
    return list_of_things

first_list_of_things: list = (what_to_take(start_dict,15))
print(first_list_of_things)
def options_of_what_to_take (first_option: list, things: dict, max_weight: int = MAX_WEIGHT) -> list:
    another_option: list = []
    common_weight: float = 0
    for items in things.keys():
        if items in first_option:
            continue
        if common_weight + things[items] > max_weight:
            continue
        another_option.append(items)
        common_weight += things[items]
    for items in things.keys():
        if items in another_option:
            continue
        if common_weight + things[items] > max_weight:
            continue
        another_option.append(items)
        common_weight += things[items]
    print(common_weight)
    # print(another_option)
    return another_option

next_list_of_things = options_of_what_to_take(first_list_of_things,start_dict,15)
print(next_list_of_things)

def get_many_options(things: dict, max_weight = MAX_WEIGHT) -> list:
    list_of_options: list = [[]]
    quantity_of_options = int(input("How many options do you want to get? "))
    list_of_options[0] = what_to_take(things, max_weight)
    if quantity_of_options > 1:
        list_of_options.append(options_of_what_to_take(list_of_options[0],things,max_weight))
        if quantity_of_options > 2:
            count_of_opt: int = 2
            while count_of_opt<quantity_of_options:
                lst = list(set(list_of_options[count_of_opt - 2]).union(set(list_of_options[count_of_opt - 1])))
                list_of_options.append(options_of_what_to_take(lst,things,max_weight))
                count_of_opt += 1
    return list_of_options

opt = get_many_options(start_dict, 15)
print('So these are options of things: ' )
for lst in opt:
    print(lst)

