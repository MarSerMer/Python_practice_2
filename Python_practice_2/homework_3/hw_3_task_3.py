# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import  string

HOW_MANY_WORDS_NEEDED = 10
FILE_NAME = 'start_text.txt'

with open (FILE_NAME,encoding='utf-8') as f:
    start_text = f.read()

# для начала можно убрать знаки препинания и сделать единый регистр:
text_to_split = start_text.translate(str.maketrans('', '', string.punctuation)).lower()
all_words: set = set(text_to_split.split())
words_and_their_quantities: dict = {} # создаю словарь, куда нужно положить пары количество-слово:
for word in all_words:
    key = words_and_their_quantities.setdefault(text_to_split.count(word), list())
    key.append(word)
dd = sorted(words_and_their_quantities, reverse = True) # список всех количеств, отсортированный по убыванию

most_common_words: list = []
count_words: int = 0
for quantity in dd:
    for word in words_and_their_quantities[quantity]:
        if count_words == HOW_MANY_WORDS_NEEDED:
            break
        most_common_words.append(word)
        count_words += 1
print(most_common_words)

