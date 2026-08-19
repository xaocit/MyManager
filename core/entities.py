### Файл с датаклассами

from dataclasses import dataclass


@dataclass(frozen=True)
## Описываем структуру полей данных
class StructDataOfTransaction:

    # Поля структуры (класса)

    id: int  # Уникальный ID транзакции
    date: str  # Дата транзакции
    amount: float  # Сумма транзакции
    typeOp: str  # Тип операции - доход/расход
    description: str  # Заметка об операции

    # Методы 

    # Создание объекта из словаря
    @classmethod
    def from_dict(cls, data: dict) -> StructDataOfTransaction:
        return cls(
            id=data['id'],
            date=data['date'],
            amount=data['amount'],
            typeOp=data['type'],
            description=data['description']
        )

    # Преобразование объекта в словарь
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "date": self.date,
            "amount": self.amount,
            "type": self.typeOp,
            "description": self.description
        }

    