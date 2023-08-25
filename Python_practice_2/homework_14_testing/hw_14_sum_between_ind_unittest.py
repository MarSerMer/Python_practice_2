import unittest
from homework_14_testing.hw_14_sum_between_ind_doctest import sum_between_indexes

class TestSumInd(unittest.TestCase):
    def test_normal_datas(self):
        self.assertEqual(sum_between_indexes([12, 0.7, 95, 7, 0.3 ],2,70), 102.3)

    def test_zeros(self):
        self.assertEqual(sum_between_indexes([0, 0, 0, 0, 0], 1, 2),0)

    def test_strange_indexes(self):
        self.assertEqual(sum_between_indexes([-5, -12, -7, -90, -1], -10, -50),0)


if __name__ == '__main__':
    unittest.main(verbosity=2)