class Vacancy:

    def __init__(self, name: str, url: str, salary_from: int, salary_to: int, currency: str) -> None:
        self.name = name
        self.url = url
        self.salary_from = salary_from if salary_from is not None else 0
        self.salary_to = salary_to if salary_to is not None else 0
        self.currency = currency

    @staticmethod
    def is_salary(salary: dict) -> tuple:
        """
        Установленная зарплата
        :param salary: значение оплаты
        :return: зарплата <int>, если не установлена, то <"Зарплата не указана": str>
        """
        if salary:
            salary_from = salary.get('from') if salary.get('from') is not None else 0
            salary_to = salary.get('to') if salary.get('to') is not None else 0
            currency = salary.get('currency')
            return salary_from, salary_to, currency
        else:
            return 0, 0, ''

    @classmethod
    def get_vacancies(cls, name: str, url: str, salary_from: int, salary_to: int, currency: str):
        """
        Метод создает объект класса Vacancy
        :param name:
        :param url:
        :param salary_from:
        :param salary_to:
        :param currency:
        :return: класс <Vacancy>
        """
        return cls(name, url, salary_from, salary_to, currency)

    @staticmethod
    def cast_to_object_list(data: list) -> list:
        """
        Преобразование набора данных из JSON в список объектов
        :param data: лист словарей вакансий
        :return: возвращает лист объектов вакансий класса
        """
        obj_vacancies_list: list = []
        for item in data:
            name = item.get("name")
            url = item.get("alternate_url")
            salary = item.get("salary")
            salary_from, salary_to, currency = Vacancy.is_salary(salary)
            vacancy = Vacancy.get_vacancies(name, url, salary_from, salary_to, currency)
            obj_vacancies_list.append(vacancy)
        return obj_vacancies_list

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __eq__(self, other):
        return self.salary_from == other.salary_from

    def __str__(self):
        return f'Вакансия: "{self.name}", ЗП: {self.salary_from} - {self.salary_to} {self.currency}, url: {self.url}'

    def __repr__(self):
        return f'{self.__class__.__name__} -> {self.name, self.salary_from, self.salary_to, self.currency, self.url}'
