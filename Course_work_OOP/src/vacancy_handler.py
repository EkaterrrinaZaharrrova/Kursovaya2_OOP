from abc import abstractmethod

from custom_logger import get_logger

logger = get_logger()


class VacancyHandler:
    """Класс обработки вакансий"""

    @abstractmethod
    def add_vacancy(self) -> list:
        """Метод добавления вакансий."""
        pass


class JsonHandler(VacancyHandler):
    """Класс для работы с типом данных JSON."""

    list_object_vacancy: list = []

    __slots__ = ("un", "source", "name", "from", "to", "description", "city", "link")

    def __init__(
        self, source: str, uniq_num: str, name: str, from_: int, to: int, description: str, city: str, link: str
    ) -> None:
        """Конструктор класса VacancyHandler."""

        self.__uniq_num: str = JsonHandler.__validate_uniq_num(uniq_num)
        self.__source: str = JsonHandler.__validate_source(source)
        self.__name: str = JsonHandler.__validate_name(name)
        self.__from_: int = JsonHandler.__validate_from(from_)
        self.__to: int = JsonHandler.__validate_to(to)
        self.__description: str = JsonHandler.__validate_description(description)
        self.__city: str = JsonHandler.__validate_city(city)
        self.__link: str = JsonHandler.__validate_link(link)

    def __eq__(self, other) -> str | None:
        """Метод сравнения вакансий по минимальной зарплате."""

        if self.__from_ == other.__from_:
            return f"{self.__name} и {other.__name}, одинаковые."

    def __gt__(self, other) -> str | None:
        """Метод сравнения вакансий по минимальной зарплате."""

        if self.__from_ > other.__from_:
            return f"{self.__name} больше, чем {other.__name}."

    def __lt__(self, other) -> str | None:
        """Метод сравнения вакансий по минимальной зарплате."""

        if self.__from_ < other.__from_:
            return f"{self.__name} меньше, чем {other.__name}."

    def __repr__(self) -> str:
        """Вывод данных о вакансии JsonHandler,
        в удобном для чтения формате."""

        return (
            f""
            f"Название: {self.__name}\n"
            f"Оплата: {self.__from_} - {self.__to}\n"
            f"Место работы: {self.__city}\n"
            f"Загружено с : {self.__source}\n"
            f"Описание: {self.__description}....\n"
            f"Подробная информация: {self.__link}\n"
            f"_________________________________________\n"
        )

    def add_vacancy(self) -> list:
        """Метод добавления вакансий."""

        self.list_object_vacancy.append(
            JsonHandler(
                self.__uniq_num,
                self.__source,
                self.__name,
                self.__from_,
                self.__to,
                self.__description,
                self.__city,
                self.__link,
            )
        )

        return self.list_object_vacancy

    @classmethod
    def find_by_list_vacancy(cls, search_word: str) -> list:
        """Метод поиска совпадений по описанию вакансии."""

        match_list = []

        for item in cls.list_object_vacancy:
            if search_word in item.__description:
                match_list.append(item)

        return match_list

    @staticmethod
    def show_top_vacancy(list_vacancy: list, quantity: int = 5) -> list:
        """Метод отображения вакансий с самой высокой оплатой."""

        sort_list = sorted(list_vacancy, key=lambda item: item.__from_)

        return sort_list[0:quantity]

    @staticmethod
    def __validate_uniq_num(uniq_num: str) -> str:
        """Проверка входящих данных."""

        if isinstance(uniq_num, str):
            return uniq_num

        return " - "

    @staticmethod
    def __validate_source(source: str) -> str:
        """Проверка входящих данных."""

        if isinstance(source, str):
            return source

        return " - "

    @staticmethod
    def __validate_name(name: str) -> str:
        """Проверка входящих данных."""

        if isinstance(name, str):
            return name

        return " - "

    @staticmethod
    def __validate_from(from_: int) -> int:
        """Проверка входящих данных."""

        if isinstance(from_, int):
            return from_

        return 0

    @staticmethod
    def __validate_to(to: int) -> int:
        """Проверка входящих данных."""

        if isinstance(to, int):
            return to

        return 0

    @staticmethod
    def __validate_description(description: str) -> str:
        """Проверка входящих данных."""

        if isinstance(description, str):
            return description

        return " - "

    @staticmethod
    def __validate_city(city: str) -> str:
        """Проверка входящих данных."""

        if isinstance(city, str):
            return city

        return " - "

    @staticmethod
    def __validate_link(link: str) -> str:
        """Проверка входящих данных."""

        if isinstance(link, str):
            return link

        return " - "