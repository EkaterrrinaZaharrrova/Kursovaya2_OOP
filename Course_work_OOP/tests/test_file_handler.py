import os

from config import DATA_DIR
from src.file_handler import Json


def test_json_file_handler() -> None:
    """Тест класса Json."""

    filename = "test_file"
    json = Json(filename, [{"test": "data"}])
    json.create_file()
    json.read_file()
    json.update_file()
    json.delete_file()
    os.remove(DATA_DIR + filename + ".json")


def test_validate() -> None:
    """Тест валидации имени файла и типа данных файла."""

    Json()