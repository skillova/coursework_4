import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancies():
    return [
        {"name": "Python ML-разработчик (искусственный интеллект)", "alternate_url": "https://hh.ru/vacancy/95020549",
         "salary": {"from": 180000, "to": 0, "currency": "RUR"}},
        {"name": "Стажер-разработчик Python", "url": "https://hh.ru/vacancy/94354526",
         "salary": {"from": 100000, "to": 150000, "currency": "RUR"}},
        {"name": "Backend-разработчик / Python developer", "url": "https://hh.ru/vacancy/94940292",
         "salary": {"from": 100000, "to": 220000, "currency": "RUR"}}]


def test_vacancy(vacancies):
    obj =  Vacancy.cast_to_object_list(vacancies)[0]
    assert obj.name == "Python ML-разработчик (искусственный интеллект)"
    assert obj.url == "https://hh.ru/vacancy/95020549"
    assert obj.salary_from == 180000
    assert obj.salary_to == 0
    assert obj.currency == "RUR"
