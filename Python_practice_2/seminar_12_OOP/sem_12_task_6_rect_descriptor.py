# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

class SidesOfRectangle:
    def __set_name__(self, owner, name):
        self.name = '__'+name

    def __get__(self, instance, owner):
        return getattr(instance,self.name)

    def __set__(self,instance,value):
        if value > 0:
            setattr(instance,self.name, value)
        else:
            raise ValueError ('wrong datas for side')

class Rectangle:
    """
    This class is about a rectangle. Just give 2 numbers for length and width
    in order to get a rectangle, or one number in order to get a square.
    """

    side_a = SidesOfRectangle()
    side_b = SidesOfRectangle()


    def __init__(self,side_a:float, side_b:float = None):
        self.side_a = float(side_a)
        if side_b == None:
            self.side_b = float(side_a)
        else:
            self.side_b = float(side_b)

    def get_perim(self)->float:
        """
        Allows to count a perimeter of your rectangle.
        """
        return 2*(self.side_a + self.side_b)

    def get_square(self)->float:
        """
        Allows to count a square of your rectangle.
        """
        return self.side_a*self.side_b

    def __str__(self):
        return f'The rectangle. Length = {self.side_a}, width = {self.side_b}'

if __name__ == '__main__':
    r_1 = Rectangle(2,3)
    print(r_1)
    r_2 = Rectangle(-5, 12)
    print(r_2)