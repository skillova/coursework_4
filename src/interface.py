class Interface:

    @staticmethod
    def key_word() -> str:
        """
        Приведение строки к нижнему регистру
        :return: str
        """
        search_query: str = input("Введите поисковый запрос: ").lower()
        return search_query

    @staticmethod
    def top_n(obj_list: list) -> str | list:
        """
        Фильтр списка ТОП N объектов класса по ЗП (__eq__ __lt__)
        :param obj_list: список объектов класса
        :return: list(cls_obj, cls_obj, cls_obj ...)
        """
        try:
            n: str = int(input("Введите количество вакансий для вывода в топ N: "))
            sorted_obj: list = sorted(obj_list, reverse=True)
            sorted_obj = sorted_obj[:n]
        except ValueError as err:
            return str(err)
        return sorted_obj

    @staticmethod
    def filter_words(obj_list) -> list | str:
        """
        Фильтр списка объектов класса по ключевым словам
        :param obj_list: список объектов класса
        :return: list(cls_obj, cls_obj, cls_obj ...)
        """
        result: list = []
        key_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
        for word in key_words:
            for obj in obj_list:
                vacancy_name: str = obj.name.lower()
                if word in vacancy_name:
                    result.append(obj)
        if result:
            return result
        else:
            return 'Ничего не найдено'

    @staticmethod
    def salary_range(obj_list) -> ValueError | list:
        """
        Фильтр списка объектов класса по диапазону ЗП
        :param obj_list: список объектов класса
        :return: list(cls_obj, cls_obj, cls_obj ...)
        """
        result: list = []
        salary = input("Введите диапазон зарплат: ").split()
        try:
            salary_from, salary_to = map(int, salary)
        except ValueError as err:
            return err
        for obj in obj_list:
            obj_salary_from, obj_salary_to = obj.salary_from, obj.salary_to
            if salary_from <= obj_salary_from and salary_to >= obj_salary_to:
                result.append(obj)
        return result
