### Модуль с интерфейсными классами для сервиса

from abc import ABC, abstractmethod
from typing import List, Union


from core.entities import StructDataOfTransaction


class IRepository(ABC):
    """Абстрактный класс, интерфейс репозитория"""

    @abstractmethod
    def load_all(self) -> List[StructDataOfTransaction]:
        pass

    @abstractmethod
    def save_all(self, transactions: List[StructDataOfTransaction]) -> None:
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

class ITransactionReadService(ABC):

    @abstractmethod
    def get_all(self, reverse=False) -> List[StructDataOfTransaction]:
        pass

    @abstractmethod
    def get_sorted(self, field_indicies: List[int]) -> List[StructDataOfTransaction]:
        pass

    @abstractmethod
    def get_data_by_id(self, find_id: int) -> tuple[bool, Union[int | None]]:
        pass

class ITransactionWriteService(ABC):

    @abstractmethod
    def get_all(self, reverse=False) -> List[StructDataOfTransaction]:
        pass

    @abstractmethod
    def get_sorted(self, field_indicies: List[int]) -> List[StructDataOfTransaction]:
        pass

    @abstractmethod
    def get_data_by_id(self, find_id: int) -> tuple[bool, Union[int | None]]:
        pass