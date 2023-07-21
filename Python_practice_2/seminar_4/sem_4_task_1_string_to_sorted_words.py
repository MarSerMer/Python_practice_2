# Задание №1
# Погружение в Python | Функции
# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

def string_to_words(s: str):
    list_of_words: list = sorted(s.split())
    max_word_length: int = 0
    for word in list_of_words:
        if len(word) > max_word_length:
            max_word_length = len(word)
    for i,word in enumerate(list_of_words, start=1):
        print(f'{i} {word:>{max_word_length}}')


string_to_words('А роза упала на лапу Азора')