### Файл с датаклассами

from dataclasses import dataclass


@dataclass(frozen=True)
class StructDataOfTransaction:
    """Класс, описывающий, какие данные хранятся в каждой строке бд
    и предоставляющий методы для преобразования словаря в объект данных, и наоборот"""

    # Поля структуры (класса)

    id: int  # Уникальный ID транзакции
    date: str  # Дата транзакции
    amount: float  # Сумма транзакции
    typeOp: str  # Тип операции - доход/расход
    description: str  # Заметка об операции

    @classmethod
    def from_dict(cls, data: dict) -> StructDataOfTransaction:
        """Создание объекта тек. класса из словаря"""
        return cls(
            id=data['id'],
            date=data['date'],
            amount=data['amount'],
            typeOp=data['type'],
            description=data['description']
        )

    def to_dict(self) -> dict:
        """Преобразование объекта в словарь"""
        return {
            "id": self.id,
            "date": self.date,
            "amount": self.amount,
            "type": self.typeOp,
            "description": self.description
        }

    