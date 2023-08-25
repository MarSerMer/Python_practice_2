# Задание №5
# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.

import unittest
from seminar_11_OOP.sem_11_tasks_5_6_rectangle import Rectangle, RectanglePro

class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.r1 = RectanglePro(2,3)
        self.r2 = RectanglePro(7)
        self.r3 = RectanglePro(1,9)
        self.r4 = RectanglePro(1,1)

    def test_creating_rectangle(self):
        self.assertEqual(self.r1, Rectangle(2,3))

    def test_perim(self):
        self.assertEqual(self.r2.get_perim(), 28)

    def test_square(self):
        self.assertEqual(self.r3.get_square(), 9)

    def test_not_equal(self):
        self.assertNotEqual(self.r1, self.r4)

    def test_sum(self):
        self.assertEqual((self.r2 + self.r3).get_perim(), 48)

if __name__ == '__main__':
    unittest.main(verbosity=2)