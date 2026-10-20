### Файл взаимодействия программы с данными в .json - файле


# Импорты

import logging
import json, pathlib
from typing import List

from MyManager.exeptions.exceptions_of_data_manager import (
    DecoderDataBaseError,
    FileWithDataBaseFoundError,
    SaveDataBaseError
)

from MyManager.core.entities import StructDataOfTransaction

from MyManager.services.interfaces import IRepository

from MyManager.infrastructure.interfaces import IDataFormatter


# Конец импортов

# Создаём логгер для этого модуля
logger = logging.getLogger(__name__)

class JsonFormatter(IDataFormatter):
    """Класс форматирования списка из вида python в вид, характерный для .json - файла, и наоборот"""

    def from_dict(self, data: dict) -> List[StructDataOfTransaction]:
        """Преобразование словаря из JSON в список Transaction"""

        transactions_data = data.get("transactions", [])

        return [StructDataOfTransaction(id=item["id"],
                                        date=item["date"],
                                        amount=float(item["amount"]),
                                        typeOp=item["typeOp"],
                                        description=item["description"]) for item in transactions_data]
    
    def to_dict(self, transactions: List[StructDataOfTransaction]) -> dict:
        """Преобразование списка в словарь для JSON"""

        return {
            "transactions" : [
                {
                    "id": transaction.id,
                    "date": transaction.date,
                    "amount": transaction.amount,
                    "typeOp": transaction.typeOp,
                    "description": transaction.description
                } for transaction in transactions
            ]
        }

class JsonRepository(IRepository):
    """Класс-репозиторий для оперирования со списком транзакций и файлом .json"""

    def __init__(self, file_path: str | pathlib.Path, formatter: IDataFormatter):

        # Получаем абсолютный путь к файлу
        current_file = pathlib.Path(__file__).resolve()

        # Поднимаемся на уровень вверх
        project_root = current_file.parent.parent

        # Соединяем корень проекта именем файла
        self.file_path = project_root / file_path


        self.formatter = formatter

        # Убедимся, есть ли папка для файла
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    
    def load_all(self) -> List[StructDataOfTransaction]:
        """Этот метод читает файлик бд и возвращает выгруженные транзакции в виде списка"""

        try:
            with open(self.file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)

        # Исключения при ошибке расшифровки данных json
        except json.JSONDecodeError as e:
            logger.exception("Ошибка парсинга данных JSON")
            raise DecoderDataBaseError(e) from e

        except FileNotFoundError as e:
            logger.exception(f"Файл с базой данных не найден по пути: {self.file_path}")
            raise FileWithDataBaseFoundError(self.file_path) from e

        else:
            # Преобразуем json-данные в список транзакций
            return self.formatter.from_dict(data)

    def save_all(self, transactions: List[StructDataOfTransaction]) -> None:
        """Сохранение транзакций в JSON файле"""

        # Преобразуем транзакции в словарь
        data = self.formatter.to_dict(transactions)
        
        try:
            # Записываем словарик в файл
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(
                    data,
                    file,
                    indent=4,            # Красивое форматирование
                    ensure_ascii=False,  # русский язык
                    sort_keys=False      # Без сортировки ключей
                )

        # 1. Ошибка прав доступа (например, файл защищен от записи или открыт другой программой)
        except PermissionError as e:
            logger.exception(f"Нет прав на запись в файл по пути: {self.file_path}")
            raise SaveDataBaseError("Недостаточно прав для сохранения файла базы данных.") from e

        # 2. Ошибка ОС (например, закончилось место на диске, не существует указанная папка)
        except OSError as e:
            logger.exception(f"Системная ошибка ввода-вывода при сохранении в {self.file_path}")
            raise SaveDataBaseError(f"Ошибка операционной системы при сохранении данных: {e.strerror}") from e