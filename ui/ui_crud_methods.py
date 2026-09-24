### Модуль с методами CRUD на уровне ui-слоя

###### Логика импорта внешних зависимостей для проверки типов
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui_layer_validator import UiValidatorOfInputTransaction, UiValidatorOfInputId
######

from services.interfaces import ITransactionWriteService


class CRUDmenuMethods:
    """Класс, реализующий методы по запросу данных и выполнения этих операций для изменения бд"""

    def __init__(self, write_service: ITransactionWriteService,
                 ui_level_validator_transaction: UiValidatorOfInputTransaction, ui_level_validator_id: UiValidatorOfInputId):
        
        # Внешние зависимости (объекты классов других слоёв)
        self.write_service = write_service

        # Внутренние зависимости (объекты классов этого слоя)
        self.ui_level_validator_transaction = ui_level_validator_transaction
        self.ui_level_validator_id = ui_level_validator_id

    def _menu_add(self):
        """Функция запроса данных у пользователя для добавления"""

        print()
        print()

        tuple_of_new_data = self.ui_level_validator_transaction._get_validated_transaction()

        add_date, add_amount, add_type, add_description = tuple_of_new_data

        self.write_service.add(add_date, add_amount, add_type, add_description)

    def _menu_change(self):
        """Функция, соединяющая всю ui-логику для изменения данных"""

        print(end="\n\n\n")

        id_find = self.ui_level_validator_id._get_validated_id("Введите id записи, которую хотите изменить: ")

        print()

        tuple_of_new_data = self.ui_level_validator_transaction._get_validated_transaction()
        
        changed_date, changed_amount, changed_type, changed_description = tuple_of_new_data

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
        
        id_find = self.ui_level_validator_id._get_validated_id("Введите id записи, которую хотите удалить: ")

        print()

        self.write_service.delete_data(id_find)

        print("Успешно удалено.", end="\n\n")

