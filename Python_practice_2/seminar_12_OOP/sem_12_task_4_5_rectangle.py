# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.

# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.



class Rectangle:
    """
    This class is about a rectangle. Just give 2 numbers for length and width
    in order to get a rectangle, or one number in order to get a square.
    """
    __slots__ = ('__side_a', '__side_b')

    def __init__(self,side_a:float, side_b:float = None):
        self.__side_a = float(side_a)
        if side_b == None:
            self.__side_b = float(side_a)
        else:
            self.__side_b = float(side_b)

    def get_perim(self)->float:
        """
        Allows to count a perimeter of your rectangle.
        """
        return 2*(self.__side_a + self.__side_b)

    def get_square(self)->float:
        """
        Allows to count a square of your rectangle.
        """
        return self.__side_a*self.__side_b

    def __str__(self):
        return f'The rectangle. Length = {self.__side_a}, width = {self.__side_b}'

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self,value):
        if value<=0:
            raise ValueError('The side should be over zero')
        else:
            self.__side_a = float(value)

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, value):
        if value <= 0:
            raise ValueError('The side should be over zero')
        else:
            self.__side_b = float(value)


class RectanglePro(Rectangle):
    """
    This class allows to add, subtract and compare the rectangles.
    """

    def __add__(self, other):
        sum_of_perims:int = self.get_perim() + other.get_perim()
        side_a = self.side_a + other.side_a
        side_b = sum_of_perims/2 - side_a
        return RectanglePro(side_a,side_b)

    def __sub__(self, other):
        if self.get_perim() < other.get_perim():
            self, other = other, self
        diff = self.get_perim() - other.get_perim()
        side_a = abs(self.side_a - other.side_a)
        side_b = diff/2 - side_a
        return RectanglePro(side_a,side_b)

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __gt__(self,other):
        return self.get_square() > other.get_square()

    def __le__(self, other):
        return self.get_square() <= other.get_square()


if __name__ == '__main__':
    rect_1 = Rectangle(2, 3)
    rect_2 = Rectangle(5)
    print(rect_1.side_a, rect_1.side_b)
    print(rect_2.side_a, rect_2.side_b)
    rect_1.side_a = 15
    print(rect_1.side_a, rect_1.side_b)
    rect_2.side_b = -12
    print(rect_2.side_a, rect_2.side_b)