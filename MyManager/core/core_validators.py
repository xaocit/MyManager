### Модуль, реализующий валидацию на уровне ядра

from typing import Union
import re
from datetime import datetime


class ValidateId:
    """Класс для валидации id"""

    @staticmethod
    def is_correct_id(id: str) -> Union[str, bool]:

        if id.isdigit():
            if int(id) >= 0:
                return True
            
            return "Ошибка! Id должен быть >= 0 !!!"
        
        return "Ошибка! Id должен быть числом !!!"


class ValidateDate:
    """Класс, реализующий методы по валидации даты"""

    @staticmethod
    def is_correct_date(new_date: str) -> Union[str, bool]:

        try:
            datetime.strptime(new_date, "%d.%m.%Y")
            
        except ValueError as e:
            return "Ошибка! Неверный формат введённой даты или её не существует !!!"

        return True


class ValidateAmount:
    """Класс, реализующий методы по валидации Суммы"""

    @staticmethod
    def is_correct_amount(new_amount: str) -> Union[str, bool]:

        try:
            value = float(new_amount)

        except ValueError:
            return "Ошибка! Сумма должна быть числом !!!"

        if value <= 0:
            return "Ошибка! Сумма должна быть положительной !!!"

        return True

class ValidateTypeOfOperation:
    """Класс, реализующий методы по валидации типа операции"""

    @staticmethod
    def is_correct_type_of_operation(new_operation: str) -> Union[str, bool]:

        if new_operation in ("expense", "income"):
            return True

        return "Ошибка! Тип операции должен быть 'expense' или 'income' !!!"