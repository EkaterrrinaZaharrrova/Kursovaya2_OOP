from abc import abstractmethod

import requests

from custom_logger import get_logger

logger = get_logger()


class Parser:
    """Класс Parser"""

    @abstractmethod
    def __get_vacancies(self, keyword: str) -> list[dict]:
        """Метод загрузки вакансий из указанного ресурса."""

        pass

    @abstractmethod
    def return_vacancies(self, keyword: str) -> list[dict]:
        """Метод форматирования данных API.
        Убирает не нужную информацию.
        Приводит к более удобному формату."""

    pass


class HeadHunter(Parser):
    """Класс для работы с API "HeadHunter" """

    __slots__ = ("url", "headers", "params", "vacancies")

    def __init__(self) -> None:
        self.__url: str = "https://api.hh.ru/vacancies"
        self._headers: dict = {"User-Agent": "HH-User-Agent"}
        self._params: dict = {"text": "", "page": 0, "per_page": 5}
        self._vacancies: list = []
        super().__init__()

    def __get_vacancies(self, keyword: str) -> None | list[dict] | str:
        """Загрузка вакансий класс HeadHunter.
        Возвращает не обработанный JSON."""

        self._params["text"] = keyword

        while self._params.get("page") != 5:
            response = requests.get(self.__url, headers=self._headers, params=self._params)

            if response.status_code == 200:
                vacancies = response.json()["items"]
                self._vacancies.extend(vacancies)
                self._params["page"] += 1
            else:
                logger.error(f"{response.reason}")
                return f'Ошибка "{response.reason}"'

            return self._vacancies

    def return_vacancies(self, keyword: str) -> list[dict]:
        """Форматирование данных API "HeadHunter" """

        self.__get_vacancies(keyword)

        vacancies_ = []
        vacancies = []

        for item in self._vacancies:
            # замена None на свои значения

            if item["salary_range"]:

                if item["salary_range"]["from"] is None:
                    item["salary_range"]["from"] = 0
                elif item["salary_range"]["to"] is None:
                    item["salary_range"]["to"] = 0

            elif item["salary_range"] is None:
                item["salary_range"] = {"from": 0, "to": 0}

            vacancies_.append(item)

        for elem in vacancies_:
            vacancies.append(
                {
                    "source": self.__class__.__name__,
                    "uniq_num": elem["id"],
                    "name": elem["name"],
                    "from_": elem["salary_range"]["from"],
                    "to": elem["salary_range"]["to"],
                    "description": elem["snippet"]["requirement"],
                    "city": elem["area"]["name"],
                    "link": elem["apply_alternate_url"],
                }
            )

        return vacancies