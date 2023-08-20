# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

from hw_13_exceptions import SideException

class RectangleHomework13:
    """
    This class is about a rectangle. Just give 2 numbers for length and width
    in order to get a rectangle, or one number in order to get a square.
    """
    __slots__ = ('__side_a', '__side_b')

    def __init__(self,side_a:float, side_b:float = None):
        if side_a > 0:
            self.__side_a = float(side_a)
            if side_b == None:
                self.__side_b = float(side_a)
            else:
                if side_b > 0:
                    self.__side_b = float(side_b)
                else:
                    raise SideException(side_b)
        else:
            raise SideException(side_a)

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
            raise SideException(value)
        else:
            self.__side_a = float(value)

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, value):
        if value <= 0:
            raise SideException(value)
        else:
            self.__side_b = float(value)

if __name__ == '__main__':
    r_1 = RectangleHomework13(2,5)
    print(r_1)
    r_2 = RectangleHomework13(7,-12)
    print(r_2)