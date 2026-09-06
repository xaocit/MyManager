# Главный файл (Точка входа)

### Импортируем классы и данные, необходимые для запуска ###

from infrastructure.data_manager import JsonRepository, JsonFormatter

from services.data_service import TransactionService, TransactionSorter, TransactionCreatorOfNewId
from services.data_input_validator import ValidatorOfInputData

from ui.ui_service import GeneralUiClass, FactoryDependencies

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

    # Собираем в service наш кастомный json-репозиторий и свой сортер для сортировки данных
    service = TransactionService(repository, creator_of_new_id, sorter)

    # Инициализируем валидатор
    validator = ValidatorOfInputData()

    # Собираем все предыдущие объекты (service, validator) в классе по работе с консольным UI
    build_dependencies = FactoryDependencies(service, validator)

    general_ui_obj = GeneralUiClass(build_dependencies)

    # Запускаем приложение включением ui
    general_ui_obj.run()


if __name__ == "__main__":
    main()

