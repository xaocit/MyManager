# Главный файл (Точка входа)

### Импортируем классы и данные, необходимые для запуска ###

from core.core_validators import (ValidateId,
                                  ValidateDate,
                                  ValidateAmount,
                                  ValidateTypeOfOperation
)

from infrastructure.data_manager import JsonRepository, JsonFormatter

from services.data_service import (TransactionReadService, 
                                   TransactionWriteService, 
                                   TransactionSorter, 
                                   TransactionCreatorOfNewId
    )

# Импорты из ui-слоя
from ui.ui_crud_methods import CRUDmenuMethods
from ui.ui_layer_validator import (UiValidatorOfInputTransaction, 
                                   UiValidatorOfInputId, 
                                   UiValidatorOfMenuChoice)

from ui.ui_output_data_modules.ui_output_common_data import ConsoleInterfaceMessages
from ui.ui_output_data_modules.ui_output_custom_data import TransactionsOutputUI

from ui.ui_service import GeneralUiClass, RunApp

from config import DATA_FILE_PATH

### Конец импорта ###

def main():
    """Главная Функция, где собираем зависимости и запускаем ui - интерфейс"""

    # Класс форматирования списка из вида python в вид, характерный для .json - файла, и наоборот
    formatter = JsonFormatter()

    # Собираем в репозитории наш путь к файлу бд и логику форматирования (перевода) данных в formatter
    repository = JsonRepository(DATA_FILE_PATH, formatter)

    # Инициализируем объект сортера
    sorter = TransactionSorter()

    # Инициализируем объект класса для логики создания нового, свободного id
    creator_of_new_id = TransactionCreatorOfNewId()

    # Собираем в read_service и write_service наш кастомный json-репозиторий и свой сортер для сортировки данных
    read_service = TransactionReadService(repository, sorter)
    write_service = TransactionWriteService(repository, 
                                            creator_of_new_id, 
                                            read_service)


        ########## Объекты всех валидаторов - начало
    

    # Инициализируем валидаторы файлов core-слоя 
    core_validator_id = ValidateId()
    core_validator_date = ValidateDate()
    core_validator_amount = ValidateAmount()
    core_validator_type_of_operation = ValidateTypeOfOperation()

    # Инициализируем валидаторы файлов ui-слоя
    ui_validator_transaction = UiValidatorOfInputTransaction(core_validator_date, 
                                                             core_validator_amount, 
                                                             core_validator_type_of_operation)
    
    ui_validator_id = UiValidatorOfInputId(read_service, core_validator_id)
    ui_validator_choice = UiValidatorOfMenuChoice()


        ########## Объекты всех валидаторов - конец


    crud_menu_methods = CRUDmenuMethods(write_service, 
                                        ui_validator_transaction, 
                                        ui_validator_id)

    interfaces_menu = ConsoleInterfaceMessages()
    display_data_methods = TransactionsOutputUI()


    # Собираем все предыдущие объекты (service, validator) в классе по работе с консольным UI
    general_ui_obj = GeneralUiClass(read_service,
                                    interfaces_menu,
                                    ui_validator_choice,
                                    crud_menu_methods,
                                    display_data_methods)

    # Запускаем приложение включением ui

    execute_app = RunApp(general_ui_obj)
    execute_app.run()


if __name__ == "__main__":
    main()

