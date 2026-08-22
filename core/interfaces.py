### Файл с интерфейсами

from abc import ABC, abstractmethod
from typing import List

class IRepository(ABC):
    """Абстрактный класс, интерфейс репозитория"""

    @abstractmethod
    def load_all(self) -> List[StructDataOfTransaction]:
        pass

    @abstractmethod
    def save_all(self, transactions: List[StructDataOfTransaction]) -> None:
        pass


class IDataFormatter(ABC):
    """Абстрактный класс, интерфейс форматтера"""

    @abstractmethod
    def from_dict(self, data: dict) -> List[StructDataOfTransaction]:
        pass

    @abstractmethod
    def to_dict(self, transactions: List[StructDataOfTransaction]) -> dict:
        pass


class ISorter(ABC):
    """Абстрактный класс, интерфейс сортера"""

    @abstractmethod
    def my_sort(self, data: List[StructDataOfTransaction], field_indices: List[int]) -> List[StructDataOfTransaction]:
        pass

class ICreatorOfNewId(ABC):
    """Абстрактный класс, интерфейс логики формирования id для новой записи в бд"""

    @abstractmethod
    def create_new_id(self, transactions: List[StructDataOfTransaction]) -> int:
        pass
