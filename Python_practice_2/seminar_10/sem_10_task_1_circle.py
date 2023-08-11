# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

from math import pi

class Circle:
    def __init__(self,r:int):
        self.r = r

    def get_length(self)-> float:
        return pi*2*self.r

    def get_square(self)->float:
        return pi*(self.r**2)

cir_one = Circle(12)
print(cir_one.get_length())
print(cir_one.get_square())
