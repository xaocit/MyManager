# Главный файл (Точка входа)

### Импортируем классы и данные, необходимые для запуска ###

from infrastructure.data_manager import JsonRepository, JsonFormatter

from services.data_service import (
    TransactionReadService, TransactionWriteService, 
    TransactionSorter, TransactionCreatorOfNewId
    )
from services.data_input_validator import ValidatorOfInputData

from ui.ui_service import GeneralUiClass, FactoryDependencies, RunApp

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
    write_service = TransactionWriteService(repository, creator_of_new_id, read_service)

    # Инициализируем валидатор
    validator = ValidatorOfInputData()

    # Собираем все предыдущие объекты (service, validator) в классе по работе с консольным UI
    build_dependencies = FactoryDependencies(read_service, write_service, validator)

    general_ui_obj = GeneralUiClass(build_dependencies)

    # Запускаем приложение включением ui

    execute_app = RunApp(general_ui_obj)
    execute_app.run()


if __name__ == "__main__":
    main()

