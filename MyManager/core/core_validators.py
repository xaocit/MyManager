### Модуль, реализующий валидацию на уровне ядра

from typing import Union
import re
from datetime import datetime

from MyManager.exeptions.exceptions_of_core import (
    InvalidInputIdError,
    InvalidInputDateError,
    InvalidInputAmountError,
    InvalidInputTypeOfOperationError
)


class ValidateId:
    """Класс для валидации id"""

    @staticmethod
    def is_correct_id(id: str) -> Union[str, bool]:

        if not id.isdigit():
            raise InvalidInputIdError(id, "Id должен быть числом !!!")

        if int(id) < 0:
            raise InvalidInputIdError(id, "Id должен быть > 0 !!!")


class ValidateDate:
    """Класс, реализующий методы по валидации даты"""

    @staticmethod
    def is_correct_date(new_date: str) -> Union[str, bool]:

        format_of_date = r'\d{2}\.\d{2}\.\d{4}'
        if not bool(re.match(format_of_date, new_date)):
            raise InvalidInputDateError(new_date, "Неверный формат введённой даты !!!")

        try:
            datetime.strptime(new_date, "%d.%m.%Y")
            
        except ValueError:
            raise InvalidInputDateError(new_date, "Несуществующая дата !!!")


class ValidateAmount:
    """Класс, реализующий методы по валидации Суммы"""

    @staticmethod
    def is_correct_amount(new_amount: str) -> Union[str, bool]:

        try:
            value = float(new_amount)

        except ValueError:
            raise InvalidInputAmountError(new_amount, "Сумма должна быть числом !!!")

        if value <= 0:
            raise InvalidInputAmountError(new_amount, "Сумма должна быть >= 0 !!!")


class ValidateTypeOfOperation:
    """Класс, реализующий методы по валидации типа операции"""

    @staticmethod
    def is_correct_type_of_operation(new_operation: str) -> Union[str, bool]:

        if not new_operation in ("expense", "income"):
            raise InvalidInputTypeOfOperationError(new_operation, "Тип операции должен быть 'expense' или 'income' !!!")