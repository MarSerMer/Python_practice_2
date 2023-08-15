# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения


class Rectangle:
    """
    This class is about a rectangle. Just give 2 numbers for length and width
    in order to get a rectangle, or one number in order to get a square.
    """
    def __init__(self,side_a:float, side_b:float = None):
        self.side_a = float(side_a)
        if side_b == None:
            self.side_b = side_a
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


rect_1 = RectanglePro(2,3)
rect_2 = RectanglePro(5)
# print(rect_1.get_perim())
# print(rect_2.get_perim())

print(rect_1>=rect_2)
print(rect_1.get_square())
print(rect_2.get_square())

print(rect_1)
# rect_sum = rect_1+ rect_2
# print(rect_sum.get_perim())
# print(rect_sum.side_a, rect_sum.side_b)
# rect_dif = rect_1-rect_2
# print(rect_dif.get_perim())
# print(rect_dif.side_a, rect_dif.side_b)
