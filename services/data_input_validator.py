### Файл с логикой валидации данных

from typing import Union
import re

class ValidateCountOfValues():
    """Класс, реализующий методы по валидации количества переданных значений"""

    def is_correct_count_of_values(self, string_of_data: str, count_fields: int) -> Union[str, bool]:

        # Количество пробелов между полями
        count_of_spaces = count_fields - 1

        # Пытаемся распаковать строку
        if len(string_of_data.split(None, count_of_spaces)) != count_fields:
            return f"Ошибка! Вы должны передать {count_fields} значений через пробел !!!"

        # Если всё хорошо
        return True

class ValidateDate():
    """Класс, реализующий методы по валидации даты"""

    _date_format = r'\d{2}.\d{2}.\d{4}' # Формат даты

    def is_correct_date(self, new_date: str) -> Union[str, bool]:

        # Проверяем соответствие формату через рег. выр.
        if bool(re.match(self._date_format, new_date)):
            return True

        return "Ошибка! Неверный формат даты !!!"

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

        return "Ошибка! Тип операции должен быть 'expense' или 'income' !!!"

class ValidatorOfInputData(ValidateCountOfValues, ValidateDate, ValidateAmount, ValidateTypeOfOperation):
    """Класс, реализующий пользовательскую валидацию для проверки вводимых данных, 
    он же - класс-сборщик предыдущих валидаторов"""

    def is_correct_input(self, my_new_data_in_bd: str, correct_count_of_fields: int) -> Union[str, bool]:
        """Метод, реализующий валидацию введённой строки с данными"""

        # Валидируем количество переданных полей
        result_of_validate_count_of_fields = self.is_correct_count_of_values(
            my_new_data_in_bd,
            correct_count_of_fields
            )

        # В самом начале возвращаем ошибку валидации количества полей, если она есть
        if isinstance(result_of_validate_count_of_fields, str):
            return result_of_validate_count_of_fields

        correct_count_of_spaces = correct_count_of_fields - 1
        input_date, input_amount, input_operation, _ = my_new_data_in_bd.split(None, correct_count_of_spaces)
        
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

        # Возвращаем 1-ю попавшуюся ошибку
        for i in list_of_results:
            if isinstance(i, str):
                return i