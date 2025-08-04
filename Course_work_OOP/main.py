import re
import resource

from custom_logger import get_logger
from src.external_API import HeadHunter
from src.file_handler import Json
from src.vacancy_handler import JsonHandler

logger = get_logger()

head_hun = HeadHunter()


def user_interaction() -> None:
    """Основная функция взаимодействия с пользователем."""

    print("Что будем искать?")

    search_word = str(input())
    result_find = head_hun[int(resource) - 1].return_vacancies(search_word)

    for item in result_find:
        JsonHandler(**item).add_vacancy()

    print(
        """Можно уточнить поиск.
    Введите слово."""
    )

    filter_word = str(input())

    find_in_list = JsonHandler.find_by_list_vacancy(filter_word)

    for item in find_in_list:
        print(item)

    print("Сколько, показать вакансии с самой высокой оплатой?")

    while True:
        quantity_top = input("Укажите цифру!\n")
        if not re.findall(r"\d+", quantity_top):
            print("Только, цифры!")
            logger.warning(f'Неверный ввод  - "{quantity_top}"')
        else:
            break

    top_vacancy = JsonHandler.show_top_vacancy(find_in_list, int(quantity_top))

    for item in top_vacancy:
        print(item)

    print("Сохранить результаты в файл? Y / N ")
    save_to_file = str(input())

    if save_to_file.lower() == "y" or save_to_file.lower() == "н":
        print(
            """Как назвать файл?
        По умолчанию будет присвоено имя ''default_name''
        c меткой текущей даты и времени."""
        )

        file_name = str(input())

        Json(file_name, result_find).create_file()

    print("До встречи!")


if __name__ == "__main__":
    user_interaction()