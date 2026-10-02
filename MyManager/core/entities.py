### Файл с датаклассами

from dataclasses import dataclass


@dataclass(frozen=True)
class StructDataOfTransaction:
    """Класс, описывающий, какие данные хранятся в каждой строке бд"""

    # Поля структуры (класса)

    id: int  # Уникальный ID транзакции
    date: str  # Дата транзакции
    amount: float  # Сумма транзакции
    typeOp: str  # Тип операции - доход/расход
    description: str  # Заметка об операции

    