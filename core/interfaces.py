### Файл с интерфейсами

from abc import ABC, abstractmethod
from typing import List, Any

# Any здесь то же, что и StructDataOfTransaction

class IRepository(ABC):
    """Абстрактный класс, интерфейс репозитория"""

    @abstractmethod
    def load_all(self) -> List[Any]:
        pass

    @abstractmethod
    def save_all(self, transactions: List[Any]) -> None:
        pass


class IDataFormatter(ABC):
    """Абстрактный класс, интерфейс форматтера"""

    @abstractmethod
    def from_dict(self, data: dict) -> List[Any]:
        pass

    @abstractmethod
    def to_dict(self, transactions: List[Any]) -> dict:
        pass


class ISorter(ABC):
    """Абстрактный класс, интерфейс сортера"""

    @abstractmethod
    def my_sort(self, data: List[Any], field_indices: List[int]) -> List[Any]:
        pass

class ICreatorOfNewId(ABC):
    """Абстрактный класс, интерфейс логики формирования id для новой записи в бд"""

    @abstractmethod
    def create_new_id(self, transactions: List[Any]) -> int:
        pass
