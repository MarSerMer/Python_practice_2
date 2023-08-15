# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.


class Archive:
    """
    Хранит пару свойств.
    """
    _instance = None

    def __init__(self, text: str, num: int):
        print('init')
        # print(self.__name__)
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        """
        Добавляет строки и номера в списки
        """
        print('new')
        # print(cls.__name__)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nums_archive = []
            cls._instance.text_archive = []
        else:
            cls._instance.nums_archive.append(cls._instance.num)
            cls._instance.text_archive.append(cls._instance.text)
        return cls._instance

    def __str__(self):
        return f'We have text: {self.text} and number: {self.num}\nArchive of text: {Archive._instance.text_archive}\nArchive of nums: {self.nums_archive}'

    def __repr__(self):
        return f'We have text: {self.text} and number: {self.num}'


elem_1 = Archive('text1', 12)
elem_2 = Archive('text2', 1)
elem_3 = Archive('text3', 5)
# print(Archive._instance.nums_archive)
# print(elem_1._instance)

# help('__new__')
#
# print(Archive.__new__.__doc__)

print(elem_1)
print(repr(elem_1))