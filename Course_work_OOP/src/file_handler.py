import json
from abc import abstractmethod
from datetime import datetime

from config import DATA_DIR
from custom_logger import get_logger

date = datetime.now().strftime("%d%m%y_%H%M%S")
date_str = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

logger = get_logger()


class FileHandler:
    """Абстрактный класс работы с файлами."""

    @abstractmethod
    def create_file(self) -> None:
        """Метод создания файлов."""

        pass

    @abstractmethod
    def read_file(self) -> None:
        """Метод чтения файла."""

        pass

    @abstractmethod
    def update_file(self) -> None:
        """Метод обновления файла."""

        pass

    @abstractmethod
    def delete_file(self) -> None:
        """Метод удаления элементов файла."""

        pass


class Json(FileHandler):
    """Класс обработчик файлов json."""

    __slots__ = ("filename", "data")

    def __init__(self, filename: str = "", data: list[dict] = ()) -> None:

        self.data: list[dict] = Json.validate_data(data)
        self.filename = Json.validate_file_name(filename)

    @staticmethod
    def validate_data(data: list[dict]) -> list[dict]:
        """Проверка типа данных."""

        if isinstance(data, list):
            return data

        logger.info(f"Передача пустых данных в {Json.__name__}")

        return [
            {"Что-то пошло не так, поэтому": "здесь, нет данных"},
            {"Файл создан": date_str},
            {"Можно удалить": "этот файл."},
        ]

    @staticmethod
    def validate_file_name(filename) -> str:
        """Проверка имени файла."""

        if not filename:
            filename = f"{DATA_DIR}default_name_{date}.json"
            logger.info(f'Присвоено имя "{filename}"')
            return filename

        return DATA_DIR + filename + ".json"

    def create_file(self) -> None:
        """Создание файла."""

        with open(self.filename, "w", encoding="utf-8") as file:
            file.write(json.dumps(self.data, indent=4, ensure_ascii=False))

    def read_file(self) -> None:
        """Чтение файла."""

        with open(self.filename, "r", encoding="utf-8") as file:
            return json.load(file)

    def update_file(self) -> None:
        """Обновление файла."""

        with open(self.filename, "r", encoding="utf-8") as file:
            data_to_file = json.load(file)

        for elem in self.data:
            if elem not in data_to_file:
                data_to_file.append(elem)

        with open(self.filename, "w", encoding="utf-8") as file_:
            file_.write(json.dumps(data_to_file, indent=4, ensure_ascii=False))

    def delete_file(self) -> None:
        """Удаление файла."""

        with open(self.filename, "w"):
            pass