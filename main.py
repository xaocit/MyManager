# Главный файл (Точка входа)

### Импортируем классы и данные, необходимые для запуска ###

from infrastructure.data_manager import JsonRepository, JsonFormatter

from services.data_service import TransactionService, TransactionSorter
from services.data_input_validator import ValidatorOfInputData

from ui.ui_service import ConsoleUI

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

    # Собираем в service наш кастомный json-репозиторий и свой сортер для сортировки данных
    service = TransactionService(repository, sorter)

    # Инициализируем валидатор
    validator = ValidatorOfInputData()

    # Собираем все предыдущие объекты (service, validator) в классе по работе с консольным UI
    ui = ConsoleUI(service, validator)

    # Запускаем приложение включением ui
    ui.run()


if __name__ == "__main__":
    main()

