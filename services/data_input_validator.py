from typing import Union
import re

class ValidateDate():
    """Класс, реализующий методы по валидации даты"""

    _date_format = r'\d{2}.\d{2}.\d{4}' # Формат даты

    def is_correct_date(self, new_date: str) -> Union[str, bool]:

        # Проверяем соответствие формату через рег. выр.
        if bool(re.match(self._date_format, new_date)):
            return True

        return "Ошибка! Неверный формат даты"


class ValidateAmount():
    """Класс, реализующий методы по валидации Суммы"""

    def is_correct_amount(self, new_amount: str) -> Union[str, bool]:

        # Базовые проверки для числа
        if new_amount.lstrip('-').isdigit():

            if int(new_amount) > 0:
                return True
            
            return "Ошибка! Сумма должна быть положительной !!!"
        
        return "Ошибка! Сумма должна быть числом !!!"


class ValidateTypeOfOperation():
    """Класс, реализующий методы по валидации типа операции"""

    def is_correct_type_of_operation(self, new_operation: str) -> Union[str, bool]:

        if new_operation in ("expense", "income"):
            return True

        return "Ошибка! Тип операции должен быть 'expense' или 'income'"


class ValidatorOfInputData(ValidateDate, ValidateAmount, ValidateTypeOfOperation):
    """Класс-сборщик предыдущих валидаторов"""

    def is_correct_input(self, input_date: str, input_amount: str, input_operation: str) -> Union[list, bool]:

        result_of_validate_date = self.is_correct_date(input_date)
        result_of_validate_amount = self.is_correct_amount(input_amount)
        result_of_validate_type = self.is_correct_type_of_operation(input_operation)

        # Если все результаты проверок прошли
        if isinstance(result_of_validate_date, bool) and \
            isinstance(result_of_validate_amount, bool) and \
            isinstance(result_of_validate_type, bool):

            return True

        # Список результатов работ функций
        list_of_results = (result_of_validate_date, result_of_validate_amount, \
                           result_of_validate_type)

        # Формируем список ошибок для вывода
        messages_errors_of_validate = [i for i in list_of_results if isinstance(i, str)]

        return messages_errors_of_validate