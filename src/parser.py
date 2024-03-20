from abc import ABC, abstractmethod
import requests


class Parser(ABC):

    @abstractmethod
    def get_params(self, keyword: str) -> dict:
        """
        Создание параметров для запроса к сервису
        :param keyword: ключевое значение для поиска в полях вакансий
        :return: возвращает словарь ключей
        """
        pass

    @abstractmethod
    def get_vacancies(self):
        """Абстрактный метод для получения вакансий"""
        pass


class ParserVacancies(Parser):
    """Класс для работы с API hh.ru"""

    def __init__(self, keyword: str, pg: int = 0) -> None:
        """Инициализация класса"""
        self.__url: str = "https://api.hh.ru/vacancies"
        self.keyword: str = keyword
        self.page: int = pg

    def get_params(self, *args) -> dict:
        """
        Создание параметров для запроса к сервису
        :return: возвращает словарь ключей
        """
        params: dict = {
            "text": self.keyword,
            "page": self.page,
            "per_page": 10
        }
        return params

    def get_vacancies(self, params=None) -> list:
        """
        Метод для получения вакансий
        :param params: параметры поиска вакансий
        :return: список словарей найденных вакансий
        """
        # Объявляем список для добавления найденных вакансий
        vacancies_list: list = []
        # Парсим 20 страниц циклом for (20 стр х 100 вакансий = 2000 вакансий),
        # возвращаем найденные вакансии в формате json по ключу <"items">,
        # после каждой итерации добавляем вакансии в список vacancies_list,
        # метод возвращает список вакансий <[{vacancy}, {vacancy}, {vacancy}...]>
        for page in range(0, 5):
            self.page = page
            params = self.get_params(self.page)
            response = requests.get(url=self.__url, params=params)
            result: dict = response.json()["items"]
            vacancies_list.extend(result)
        return vacancies_list
