from pprint import pprint

from src.interface import Interface
from src.file_saver import SimpleFileSaver
from src.parser import ParserVacancies
from src.vacancy import Vacancy
import pathlib

path = pathlib.Path.cwd() / 'data' / 'vacancies_data.json'


if __name__ == '__main__':
    # Ввод ключевого слова -> str
    search_query: str = Interface.key_word()
    # Парсинг hh.ru по ключевому слову, возвращаем данные в формате JSON -> [{vac}, {vac}, ...]
    data: list = ParserVacancies(search_query).get_vacancies()
    # Данные JSON преобразуем в объекты класса Vacancy -> [<obj.Vacancy>, <obj.Vacancy>, ...]
    vacancies_obj = Vacancy.cast_to_object_list(data)
    # Фильтр ТОП N вакансий
    top_n = Interface.top_n(vacancies_obj)
    pprint(top_n)
    # Фильтр по ключевому слову
    job_filter = Interface.filter_words(top_n)
    pprint(job_filter)
    # Фильтр по диапазону ЗП в формате (пример: 100 200)
    salary_filter = Interface.salary_range(job_filter)
    pprint(salary_filter)
    # Сохранить вакансии в JSON
    file_save = SimpleFileSaver().save_data(path, salary_filter)
    # Возвращаем данные из джейсон в список объектов класса Vacancy
    file_read = SimpleFileSaver().get_data(path)
    pprint(file_read)
