### Модуль, реализующий валидацию на уровне ядра

from typing import Union
import re

class ValidateId:
    """Класс для валидации id"""

    def is_correct_id(self, id: str) -> Union[str, bool]:

        if id.isdigit():
            if int(id) >= 0:
                return True
            
            return "Ошибка! Id должен быть >= 0 !!!"
        
        return "Ошибка! Id должен быть числом !!!"

class ValidateDate:
    """Класс, реализующий методы по валидации даты"""

    _date_format = r'\d{2}.\d{2}.\d{4}' # Формат даты

    def is_correct_date(self, new_date: str) -> Union[str, bool]:

        # Проверяем соответствие формату через рег. выр.
        if bool(re.match(self._date_format, new_date)):
            return True

        return "Ошибка! Неверный формат даты !!!"


class ValidateAmount:
    """Класс, реализующий методы по валидации Суммы"""

    def is_correct_amount(self, new_amount: str) -> Union[str, bool]:

        # Базовые проверки для числа
        if new_amount.lstrip('-').isdigit():

            if int(new_amount) > 0:
                return True
            
            return "Ошибка! Сумма должна быть положительной !!!"
        
        return "Ошибка! Сумма должна быть числом !!!"


class ValidateTypeOfOperation:
    """Класс, реализующий методы по валидации типа операции"""

    def is_correct_type_of_operation(self, new_operation: str) -> Union[str, bool]:

        if new_operation in ("expense", "income"):
            return True

        return "Ошибка! Тип операции должен быть 'expense' или 'income' !!!"