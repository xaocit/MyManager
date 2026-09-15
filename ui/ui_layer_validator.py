### Модуль с классами/методами с логикой валидаторов на уровне ui-слоя

from services.data_service import TransactionReadService  # Зависим от конкретных реализаций !!!
from services.data_input_validator import ValidatorOfInputData  # Зависим от конкретных реализаций !!!

class UiValidatorOfInputData:
    """Класс, реализующий простую валидацию различных вводимых значений в различных сценариях на уровне ui-слоя"""

    def __init__(self, read_service: "TransactionReadService", validator: "ValidatorOfInputData"):
        # Внешние зависимости (объекты классов других файлов)
        self.read_service = read_service
        self.validator = validator
    
    def _data_entry_logic(self):
            """Метод, реализующий логику вывода ошибок, если они есть при добавлении или изменении записи
            Возвращает введённые данные, если они прошли проверки"""
    
            print()
            print("Введите строку с новыми данными через пробелы (например: 24.05.2024 600 income Вознаграждение за мойку посуды): ")
    
            while True:
    
                my_new_data_in_bd = input()
                
                # Отлавливаем ошибки, если валидация прошла неуспешно
                result_validate = self.validator.is_correct_input(my_new_data_in_bd, 4)
    
                # list - если ошибки связаны с неверным форматом полей
                # str - если возникла ошибка с количеством
                if isinstance(result_validate, str):
                    print()
                    print(f"Найдена ошибка в вводе: {result_validate}", end="\n\n")
                    print("Попробуйте ещё раз ввести строку: ", end="\n\n")
                else:
                    break
    
            print()
    
            new_date, new_amount, new_type, new_description = my_new_data_in_bd.split(None, 3)
            return (new_date, new_amount, new_type, new_description)
    
    def _get_validated_id(self, prompt):
        """Метод валидации вводимого id при изменении, удалении записи.
        Если всё успешно - возвращает введённый id"""

        while True:

            print(prompt)
            
            try: 
                id_find = int(input())

                if id_find < 0:
                    print()
                    print("Id должен быть больше нуля !!! Попробуйте ещё раз.", end="\n\n")
                    continue

                # Берём только 0-й индекс, поскольку нам нужно только bool - значение
                if not (self.read_service.get_data_by_id(id_find)[0]):
                    print()
                    print(f"Запись с {id_find} не найдена в базе !!! Попробуйте ещё раз.", end="\n\n")

                else:
                    return id_find

            except ValueError:
                print()
                print("Id должен быть числом !!!")
    
    def _get_validated_my_choice(self, min_value: int, max_value: int):
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
