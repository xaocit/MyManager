### Модуль с интерфейсными классами для инфраструктуры

from abc import ABC, abstractmethod
from typing import List


from core.entities import StructDataOfTransaction


class IDataFormatter(ABC):
    """Абстрактный класс, интерфейс форматтера"""

    @abstractmethod
    def from_dict(self, data: dict) -> List[StructDataOfTransaction]:
        pass

    @abstractmethod
    def to_dict(self, transactions: List[StructDataOfTransaction]) -> dict:
        pass