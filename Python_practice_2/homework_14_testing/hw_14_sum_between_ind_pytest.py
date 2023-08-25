import pytest
from homework_14_testing.hw_14_sum_between_ind_doctest import sum_between_indexes

def test_normal_datas():
    assert sum_between_indexes([12, 0.7, 95, 7, 0.3 ],2,70) == 102.3

def test_zeros():
    assert sum_between_indexes([0, 0, 0, 0, 0], 1, 2) == 0

def test_strange_indexes():
    assert sum_between_indexes([-5, -12, -7, -90, -1], -10, -50) == 0


if __name__ == '__main__':
    pytest.main(['-v'])