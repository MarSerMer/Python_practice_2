# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import time

class MyString(str):
    """
    If you use string, this class will also show you creator's name and time of creating an object
    """

    def __new__(cls,text:str,creator:str):
        """
        Gives extra information about your string
        """
        print('New started')
        instance = super().__new__(cls,text)
        instance.creator = creator
        instance.time = time.time()
        return instance

    def __str__(self):
        """
        Shows not only text, but also creator's name and time of creating
        """
        return f'{super().__str__()} created by: {self.creator} at {self.time}'

example = MyString('text','name')
example_1 = MyString('text2','name2')

print(example)
print(example_1)

print(MyString.__str__.__doc__)