# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

from numpy import array


class MyMatrix():
    """
    Class to work with matrices.
    Please fill your matrix with int or float to get the correct work.
    The objects of this class are comparable, and also you can make an addition
    and multiplication of matrices.
    """

    _columns = None
    _rows = None
    _matrix: list[list[int]] = None

    def __init__(self, incoming: list[[]]):
        """
        Initializes a new MyMatrix object.
        Please make sure the incoming is OK: all rows should be tha same length!
        """
        self._columns = len(incoming)
        self._rows = len(incoming[0])
        self._matrix = incoming

    def __str__(self):
        """
        Allows to see tne matrix on the screen.
        """
        res = ''
        for v in self._matrix:
            res = f'{res}\n{v}'
        return res

    def compare_sizes(self, other):
        if  self._columns != other._columns or self._rows != other._rows:
            return False
        return True

    def __eq__(self, other):
        if self.compare_sizes(other):
            for i in range(0, self._rows):
                for j in range(0, self._columns):
                    if self._matrix[i][j] != other._matrix[i][j]:
                        return False
            return True
        else:
            return False

    def __gt__(self, other):
        if self.compare_sizes(other):
            for i in range(0, self._columns):
                for j in range(0, self._rows):
                    if self._matrix[i][j] < other._matrix[i][j]:
                        return False
            return True
        else:
            return False

    def __le__(self, other):
        if self.compare_sizes(other):
            for i in range(0, self._columns):
                for j in range(0, self._rows):
                    if self._matrix[i][j] >= other._matrix[i][j]:
                        return False
            return True
        else:
            return False

    def __add__(self, other):
        if self.compare_sizes(other):
            res = [[0 for _ in range(self._columns)] for _ in range(self._rows)]
            for i in range(0, self._columns):
                for j in range(0, self._rows):
                    res[i][j] = self._matrix[i][j] + other._matrix[i][j]
            return MyMatrix(res)
        else:
            print('These matrices can not be added to each other')
            return None

    def __mul__(self, other):
        if self._rows == other._columns and self._columns == other._rows:
            res = [[0 for _ in range(self._rows)] for _ in range(self._columns)]
            for i in range(0, self._columns):
                for j in range(0, self._rows):
                    res[i][j] = self._matrix[i][j] * other._matrix[j][i]
            return MyMatrix(res)
        else:
            print('These matrices can not be multiplicated to each other.')
            return None

if __name__ == '__main__':
    m_1 = MyMatrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    m_2 = MyMatrix([[5, 5, 5], [5, 5, 5], [5, 5, 5]])
    m_3 = MyMatrix([[0, 0, 0], [0, 0, 0], [0, 0, 2]])
    m_4 = MyMatrix([[4,4,4],[4,2,1]])

    print(m_1, m_2, m_3)


    print(m_1 > m_2)
    print(m_1 < m_3)
    print(m_1 == m_2)
    print(m_1 + m_2)
    print(m_1 + m_3)
    print('')
    print(m_1*m_3)
    print(m_1*m_4)
