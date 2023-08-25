# Задание №3
# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import unittest

from seminar_14.sem_14_task_1_delete_symbols import validate_string


class TestValidateString(unittest.TestCase):

    def test_return_no_diff(self):
        self.assertEqual(validate_string('ff ll h'), 'ff ll h')

    def test_ret_all_in_lower(self):
        self.assertEqual(validate_string('FF LL h'), 'ff ll h')

    def test_ret_del_punctuation(self):
        self.assertEqual(validate_string('FF LL -:h'), 'ff ll h')

    def test_ret_without_not_latin_letters(self):
        self.assertEqual(validate_string('ff ll hГеннадий'), 'ff ll h')

    def test_ret_only_lat_and_spaces_in_lower(self):
        self.assertEqual(validate_string('ff ll -:hГеннадий'), 'ff ll h')


if __name__ == '__main__':
    unittest.main(verbosity=2)