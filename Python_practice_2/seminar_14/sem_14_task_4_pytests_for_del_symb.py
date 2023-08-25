# Задание №4
# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import pytest
from sem_14_task_1_delete_symbols import validate_string


def test_return_no_diff():
    assert validate_string('ff ll h') == 'ff ll h'


def test_ret_all_in_lower():
    assert validate_string('FF LL h') == 'ff ll h'


def test_ret_del_punctuation():
    assert validate_string('FF LL -:h') == 'ff ll h'


def test_ret_without_not_latin_letters():
    assert validate_string('ff ll hГеннадий') == 'ff ll h'


def test_ret_only_lat_and_spaces_in_lower():
    assert validate_string('ff ll -:hГеннадий') == 'ff ll h'


if __name__ == '__main__':
    pytest.main(['-vv'])
