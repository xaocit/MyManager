### Файл с интерфейсами

from abc import ABC, abstractmethod
from typing import List

class IRepository(ABC):

    @abstractmethod
    def load_all(self) -> List[StructDataOfTransaction]:
        pass

    @abstractmethod
    def save_all(self, transactions: List[StructDataOfTransaction]) -> None:
        pass


class IDataFormatter(ABC):

    @abstractmethod
    def from_dict(self, data: dict) -> List[StructDataOfTransaction]:
        pass

    @abstractmethod
    def to_dict(self, transactions: List[StructDataOfTransaction]) -> dict:
        pass


class ISorter(ABC):

    @abstractmethod
    def my_sort(self, data: List[StructDataOfTransaction], field_indices: List[int]) -> List[StructDataOfTransaction]:
        pass

