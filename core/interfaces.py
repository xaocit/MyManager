### Файл с интерфейсами

from abc import ABC, abstractmethod


class IRepository:

    @abstractmethod
    def load_all() -> List[StructDataOfTransaction]:
        pass

    @abstractmethod
    def save_all(transactions: List[StructDataOfTransaction]) -> None:
        pass


class IDataFormatter:

    @abstractmethod
    def from_dict(data: dict) -> List[StructDataOfTransaction]:
        pass

    @abstractmethod
    def to_dict(transactions: List[StructDataOfTransaction]) -> dict:
        pass


class ISorter:

    @abstractmethod
    def my_sort(data: List[StructDataOfTransaction], field_indices: List[int]) -> List[StructDataOfTransaction]:
        pass

