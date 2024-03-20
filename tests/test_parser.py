import pytest

from src.parser import ParserVacancies


def test_get_params():
    test = ParserVacancies("python").get_vacancies()[0]
    assert test['id'] == '95138876'
    assert test['name'] == 'Программист-стажер'