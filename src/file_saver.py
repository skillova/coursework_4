from abc import ABC, abstractmethod
import json

from src.vacancy import Vacancy


class FileSaver(ABC):

    @staticmethod
    @abstractmethod
    def get_data(file_json):
        pass

    @staticmethod
    @abstractmethod
    def save_data(file_json, data):
        pass

    @staticmethod
    @abstractmethod
    def delete_data(file_json):
        pass


class SimpleFileSaver(FileSaver):

    @staticmethod
    def get_data(file_json) -> list:
        """
        Функция возвращает данные из файла JSON и создает из него список объектов класса
        :param file_json:
        :return: list[dict, ...]
        """
        res_obj_list = []
        with open(file=file_json, mode="r", encoding="UTF-8") as file:
            data: list = json.load(fp=file)
            for vac in data:
                name = vac.get('name')
                url = vac.get('url')
                salary_from = vac.get('salary_from')
                salary_to = vac.get('salary_to')
                currency = vac.get('currency')
                res = Vacancy(name, url, salary_from, salary_to, currency)
                res_obj_list.append(res)
            return res_obj_list

    @staticmethod
    def save_data(file_json, obj_list):
        """
        Функция сохраняет объекты класса в файл JSON
        :param file_json:
        :param obj_list:
        :return:
        """
        data_to_json = []
        try:
            for obj in obj_list:
                obj_dict = {'name': obj.name, 'url': obj.url, 'salary_from': obj.salary_from,
                            'salary_to': obj.salary_to, 'currency': obj.currency}
                data_to_json.append(obj_dict)
        except ValueError as err:
            print(str(err))
        with open(file=file_json, mode="w", encoding="UTF-8") as file:
            json.dump(obj=data_to_json, fp=file, ensure_ascii=False, indent=4)

    @staticmethod
    def delete_data(file_json):
        """
        Функция удаляет данные из файла JSON
        :param file_json:
        :return:
        """
        with open(file=file_json, mode="w", encoding="UTF-8") as file:
            json.dump(obj=[], fp=file, indent=4)
