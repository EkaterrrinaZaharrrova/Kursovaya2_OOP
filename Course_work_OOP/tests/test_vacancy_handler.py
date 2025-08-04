from _pytest.capture import CaptureFixture

from src.vacancy_handler import JsonHandler


def test_cls_json_handler(return_vacancies_api: dict) -> None:
    """Тест класса JsonHandler"""

    JsonHandler(**return_vacancies_api["items"])


def test_cls_json_handler_wrong(return_vacancies_wrong: dict) -> None:
    """Тест валидации неверных данных класса JsonHandler"""

    JsonHandler(**return_vacancies_wrong)


def test_cls_json_handler_capsys(capsys: CaptureFixture, return_vacancies_api: dict) -> None:
    """Тест вывода в консоль  __str__ ."""

    JsonHandler(**return_vacancies_api["items"]).__str__()

    check_out = capsys.readouterr()

    assert check_out.out == ""


def test_dunder_methods() -> None:
    """Тест методов сравнения экземпляров класса JsonHandler."""

    JsonHandler.list_object_vacancy = []

    inst_1 = JsonHandler("uv", "fg=d6)(7g", "N-1", 456, 789, "Butchers", "tower 17", "www._oOo_.u")
    inst_2 = JsonHandler("py", "e7r6+5_6", "N-2", 123, 456, "Bay", "tower 19", "www._oOo_.u")
    inst_3 = JsonHandler("ve", "e7Q6+5_6", "N-3", 123, 456, "escape", "upper mine", "www._oOo_.u")

    check_1 = inst_2 == inst_3
    check_2 = inst_1 > inst_2
    check_3 = inst_2 < inst_1

    assert check_1 == "N-2 и N-3, одинаковые."
    assert check_2 == "N-1 больше, чем N-2."
    assert check_3 == "N-2 меньше, чем N-1."


def test_find_by_list_vacancy() -> None:
    """Тест поиска по списку вакансий."""

    JsonHandler.list_object_vacancy = []

    JsonHandler("uv", "fg=d6)(7g", "N-1", 456, 789, "Butchers", "tower 17", "www._oOo_.u").add_vacancy()
    JsonHandler("py", "e7r6+5_6", "N-2", 123, 456, "Bay", "tower 19", "www._oOo_.u").add_vacancy()
    JsonHandler("ve", "e7Q6+5_6", "N-3", 123, 456, "escape", "upper mine", "www._oOo_.u").add_vacancy()

    JsonHandler.find_by_list_vacancy("escape")


def test_show_top_vacancy() -> None:
    """Тест сортировки и вывода топ N вакансий."""

    JsonHandler.list_object_vacancy = []

    list_vacancy = [
        JsonHandler("uv", "fg=d6)(7g", "N-1", 456, 789, "Butchers", "tower 17", "www._oOo_.u"),
        JsonHandler("py", "e7r6+5_6", "N-2", 123, 456, "Bay", "tower 19", "www._oOo_.u"),
        JsonHandler("ve", "e7Q6+5_6", "N-3", 123, 456, "escape", "upper mine", "www._oOo_.u"),
    ]
    JsonHandler.show_top_vacancy(list_vacancy, 1)