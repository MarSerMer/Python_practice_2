import unittest
from homework_14_testing.hw_14_check_date_doctest import check_if_date_exists

class TestCheckDates(unittest.TestCase):
    def test_huge_strange_date(self):
        self.assertEqual(check_if_date_exists('215.40.22'), False)

    def test_normal_date(self):
        self.assertEqual(check_if_date_exists('15.01.1986'), True)

    def test_if_user_is_genius(self):
        with self.assertRaises(ValueError):
            check_if_date_exists('Capibara')

if __name__ == '__main__':
    unittest.main(verbosity=2)