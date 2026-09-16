### Модуль с методами CRUD на уровне ui-слоя

###### Логика импорта внешних зависимостей для проверки типов
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui_layer_validator import UiValidatorOfInputData
######

from services.data_service import TransactionWriteService  # Зависим от конкретных реализаций !!!
from services.domain_validator import DomainValidator  # Зависим от конкретных реализаций !!!


class CRUDmenuMethods:
    """Класс, реализующий методы по запросу данных и выполнения этих операций для изменения бд"""

    def __init__(self, write_service: "TransactionWriteService", validator: "DomainValidator",
                 ui_level_validator: "UiValidatorOfInputData"):
        # Внешние зависимости (объекты классов других файлов)
        self.write_service = write_service
        self.validator = validator

        # Внутренние зависимости (объекты классов этого файла)
        self.ui_level_validator = ui_level_validator

    def _menu_add(self):
        """Функция запроса данных у пользователя для добавления"""

        print()
        print()

        tuple_of_new_data = self.ui_level_validator._data_entry_logic()

        add_date, add_amount, add_type, add_description = tuple_of_new_data

        self.write_service.add(add_date, add_amount, add_type, add_description)

    def _menu_change(self):
        """Функция, соединяющая всю ui-логику для изменения данных"""

        print(end="\n\n\n")

        # Получаем корректный id
        id_find = self.ui_level_validator._get_validated_id("Введите id записи, которую хотите изменить: ")

        print()

        # Получаем корректные данные, если они прошли проверки
        tuple_of_new_data = self.ui_level_validator._data_entry_logic()
        
        changed_date, changed_amount, changed_type, changed_description = tuple_of_new_data

        # Меняем в списке 1 элемент
        self.write_service.change_data(
            id_find, 
            changed_date, 
            changed_amount, 
            changed_type, 
            changed_description
            )

    def _menu_delete(self):
        """ui-логика, связанная с удалением данных по id"""

        print(end="\n\n\n")
        
        # Получаем корректный id
        id_find = self.ui_level_validator._get_validated_id("Введите id записи, которую хотите удалить: ")

        print()

        # Удаляем в списке 1 элемент
        self.write_service.delete_data(id_find)

        print("Успешно удалено.", end="\n\n")

