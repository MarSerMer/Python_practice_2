# Задание №6
# Погружение в Python | Коллекции
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

start_string: str = input('Please enter some string: ')

list_of_words = sorted(start_string.split())
print(list_of_words)

word_length = 0
for words in list_of_words:
    if len(words) > word_length:
        word_length = len(words)


for i,word in enumerate(list_of_words, start = 1):
    print(f'{i} {word:>{word_length}}')