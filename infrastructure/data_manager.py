### Файл взаимодействия программы с данными в .json - файле


# Импорты

import json, commentjson, pathlib
from core.interfaces import IRepository, IDataFormatter
from core.entities import StructDataOfTransaction

# Форматтер для преобразования данных
class JsonFormatter(IDataFormatter):

    # Преобразование словаря из JSON в список Transaction
    def from_dict(data: dict) -> List[StructDataOfTransaction]:

        transactions_data = data.get("transactions", [])

        return [StructDataOfTransaction.from_dict(item) for item in transactions_data]


    # Преобразование списка в словарь для JSON
    def to_dict(transactions: List[StructDataOfTransaction]) -> dict:

        return {
            "transactions" : [
                transaction.to_dict() for transaction in transactions
            ]
        }



# Репозиторий для работы с файлом JSON
class JsonRepository(IRepository):

    def __init__(self, file_path: str, formatter: IDataFormatter):

        self.file_path = pathlib.Path(file_path)
        self.formatter = formatter

        # Убедимся, есть ли папка для файла
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    # Читает JSON
    def load_all(self) -> List[StructDataOfTransaction]:

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
        except Exception:
            pass


    # Сохранение транзакций в JSON файле
    def save_all(self, transactions: List[StructDataOfTransaction]) -> None:

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


    # Метод добавления транзакции
    def add(self, transaction: StructDataOfTransaction) -> None:

        transactions = self.load_all()

        transactions.append(transaction)

        self.save_all(transactions)


    # Метод удаления транзакции
    def delete(self, transaction_id: int) -> bool:

        transactions = self.save_all()

        for i, t in enumerate(transactions):
            if t.id == transaction_id:

                del transactions[i]

                self.save_all(transactions)
                return True

        return False

    # Изменить существующую транзакцию
    def update(self, transaction: StructDataOfTransaction) -> bool:

        transactions = self.load_all()

        for i, t in enumerate(transactions):
            if t.id == transaction.id:

                transactions[i] = transaction

                self.save_all(transactions)
                return True

        return False