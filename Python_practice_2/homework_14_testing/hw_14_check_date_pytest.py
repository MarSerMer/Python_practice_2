import pytest
from homework_14_testing.hw_14_check_date_doctest import check_if_date_exists

def test_huge_strange_date():
    assert check_if_date_exists('215.40.22') == False

def test_normal_date():
    assert check_if_date_exists('15.01.1986') == True

def test_if_user_is_genius():
    with pytest.raises(ValueError):
        check_if_date_exists('Capibara')


if __name__ == '__main__':
    pytest.main(['-v'])

