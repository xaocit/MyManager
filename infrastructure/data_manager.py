### Файл взаимодействия программы с данными в .json - файле


# Импорты

import json, commentjson, pathlib
from typing import List

from core.interfaces import IRepository, IDataFormatter
from core.entities import StructDataOfTransaction

# Конец импортов

class JsonFormatter(IDataFormatter):
    """Класс форматирования списка из вида python в вид, характерный для .json - файла, и наоборот"""

    def from_dict(self, data: dict) -> List[StructDataOfTransaction]:
        """Преобразование словаря из JSON в список Transaction"""

        transactions_data = data.get("transactions", [])

        return [StructDataOfTransaction.from_dict(item) for item in transactions_data]

    def to_dict(self, transactions: List[StructDataOfTransaction]) -> dict:
        """Преобразование списка в словарь для JSON"""

        return {
            "transactions" : [
                transaction.to_dict() for transaction in transactions
            ]
        }

class JsonRepository(IRepository):
    """Класс-репозиторий для оперирования со списком транзакций и файлом .json"""

    def __init__(self, file_path: str, formatter: IDataFormatter):

        self.file_path = pathlib.Path(file_path)
        self.formatter = formatter

        # Убедимся, есть ли папка для файла
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    
    def load_all(self) -> List[StructDataOfTransaction]:
        """Этот метод читает файлик бд и возвращает выгруженные транзакции в виде списка"""

        try:
            # Проверка наличия файла
            if not self.file_path.exists():
                print(f"!!! Файл {self.file_path} не найден. Создание нового..")
                return []

            with open(self.file_path, 'r', encoding="utf-8") as file:
                data = commentjson.load(file)

            # Преобразуем JSON в список транзакций
            return self.formatter.from_dict(data)

        ## Какие-то исключения
        except Exception as e:
            print(f"!!! Неизвестная ошибка: {e}")
            return []  # ✅ Всегда возвращаем список

    def save_all(self, transactions: List[StructDataOfTransaction]) -> None:
        """Сохранение транзакций в JSON файле"""

        try:
            # Преобразуем транзакции в словарь
            data = self.formatter.to_dict(transactions)

            # Записываем словарик в файл
            with open(self.file_path, 'w', encoding='utf-8') as file:
                commentjson.dump(
                    data,
                    file,
                    indent=4,            # Красивое форматирование
                    ensure_ascii=False,  # русский язык
                    sort_keys=False      # Без сортировки ключей
                )

        except Exception:
            pass

    def add(self, transaction: StructDataOfTransaction) -> None:
        """Метод добавления транзакции в список и обновление файла этим списком с новой записью"""

        transactions = self.load_all()

        transactions.append(transaction)

        self.save_all(transactions)

    def delete(self, transaction_id: int) -> bool:
        """Метод удаления транзакции из списка по её id и последующего обновления файла"""

        transactions = self.load_all()

        for i, t in enumerate(transactions):
            if t.id == transaction_id:

                del transactions[i]

                self.save_all(transactions)
                return True

        return False

    def update(self, transaction: StructDataOfTransaction) -> bool:
        """Метод изменения транзакции в списке по её id и последующего обновления файла"""

        transactions = self.load_all()

        for i, t in enumerate(transactions):
            if t.id == transaction.id:

                transactions[i] = transaction

                self.save_all(transactions)
                return True

        return False