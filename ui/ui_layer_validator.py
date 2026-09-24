### Модуль с классами/методами с логикой валидаторов на уровне ui-слоя

from typing import Union

from core.core_validators import (
    ValidateId,
    ValidateDate,
    ValidateAmount,
    ValidateTypeOfOperation
)

from services.interfaces import ITransactionReadService


class UiValidatorOfInputTransaction:
    """Класс, реализующий простую валидацию при вводе нового или изменения значения в бд"""

    def __init__(self, 
                 validator_date: ValidateDate, 
                 validator_amount: ValidateAmount, 
                 validator_type_of_operation: ValidateTypeOfOperation):
        
        # Внешние зависимости (объекты классов других файлов)

        self._validator_date = validator_date
        self._validator_amount = validator_amount
        self._validator_type_of_operation = validator_type_of_operation


    def _read_raw_input(self) -> str:
        """Метод чтения вводимых данных"""

        my_new_data_in_bd = input()

        return my_new_data_in_bd

    def is_correct_count_of_values(self, string_of_data: str, count_fields: int) -> Union[str, bool]:
        """Метод для валидации кол-ва переданных значений через пробел"""

        count_of_spaces = count_fields - 1

        if len(string_of_data.split(None, count_of_spaces)) != count_fields:
            return f"Ошибка! Вы должны передать {count_fields} значений через пробел !!!"

        return True

    def _parse_input(self, raw: str) -> tuple[str, str, str, str]:
        """Метод разбиения строки на поля данных"""

        return raw.split(None, 3)

    def _validate_all_fields(self, date, amount, type_of_operation) -> list[Union[str, bool]]:
        """Метод валидации отпарсенных данных"""

        result_validation_of_date = self._validator_date.is_correct_date(date)
        result_validation_of_amount = self._validator_amount.is_correct_amount(amount)
        result_validation_of_type_of_operation = self._validator_type_of_operation.is_correct_type_of_operation(type_of_operation)

        # Формируем список с валидациями
        list_of_result_validations = [
            result_validation_of_date,
            result_validation_of_amount,
            result_validation_of_type_of_operation
        ]

        return list_of_result_validations

    
    def _get_validated_transaction(self):  # Не хорошо! Разделить на методы
            """Метод, возвращающий отвалидированные данные"""
    
            print()
            print("Введите строку с новыми данными через пробелы (например: 24.05.2024 600 income Вознаграждение за мойку посуды): ")
    
            while True:
    
                my_new_data_in_bd = self._read_raw_input()

                # 1. Валидируем кол-во значений
                result_validation_of_count_values = self.is_correct_count_of_values(my_new_data_in_bd, 4)

                #1.1. Если не прошли валидацию по кол-ву - заново запрашиваем ввод
                if isinstance(result_validation_of_count_values, str):
                    print(result_validation_of_count_values)
                    print("Попробуйте ещё раз ввести данные.", end="\n\n")
                    continue

                date, amount, type_of_operation, description = self._parse_input(my_new_data_in_bd)

                list_of_result_validations = self._validate_all_fields(date, amount, type_of_operation)

                # Если все результаты валидаций принадлежат типу bool - то True, иначе (типу str), то False
                if all([isinstance(result, bool) for result in list_of_result_validations]):
                    return (date, amount, type_of_operation, description)  # Возвращаем данные в случае успешной проверки
 
                print(*[i for i in list_of_result_validations if isinstance(i, str)], sep="\n\n")  # Иначе пишем найденные ошибки
                print()
                print("Попробуйте ещё раз ввести данные.", end="\n\n")


class UiValidatorOfInputId:
    """Класс для методов валидации вводимого id"""

    def __init__(self, read_service: ITransactionReadService, validator_id: ValidateId):
        # Внешние зависимости (объекты классов других файлов)
        self.read_service = read_service
        self.validator_id = validator_id

    def _validate_format(self, id_str) -> Union[str, bool]:
        """Метод, валидирующий формат id"""

        return self.validator_id.is_correct_id(id_str)

    def _check_exist_id(self, id: str):
        """Метод проверяет существование id"""
        return self.read_service.get_data_by_id(int(id))[0]

    def _get_validated_id(self, prompt) -> int:
        """Метод валидации вводимого id при изменении, удалении записи.
        Если всё успешно - возвращает введённый id"""

        while True:

            print(prompt)
            
            input_id_by_user = input()

            result_of_id_validation = self._validate_format(input_id_by_user)

            # Валидация на уровне core
            if isinstance(result_of_id_validation, str):
                print(result_of_id_validation, end="\n\n")
                continue

            # Валидация на уровне сервиса. Берём только 0-й индекс, поскольку нам нужно только bool - значение
            if not (self._check_exist_id(input_id_by_user)):
                print()
                print(f"Запись с {int(input_id_by_user)} не найдена в базе !!! Попробуйте ещё раз.", end="\n\n")

            else:
                return int(input_id_by_user)


class UiValidatorOfMenuChoice:
    """Класс, предназначенный для валидации вводимого выбора меню пользователем"""

    def _get_validated_my_choice(self, min_value: int, max_value: int) -> int:
        """Метод для валидации выбора пользователя в различных меню"""

        while True:

            try:
                user_choice = int(input("Сделайте выбор: "))

                if min_value <= user_choice <= max_value:
                    return user_choice

                else:
                    print()
                    print(f"Введите значение с {min_value} до {max_value} !!!", end="\n\n")
                    continue

            except ValueError:
                print()
                print("Введите число !!!", end="\n\n")