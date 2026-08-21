# Главный файл (Точка входа)

from infrastructure.data_manager import JsonRepository, JsonFormatter

from services.data_service import TransactionService, TransactionSorter
from services.data_input_validator import ValidatorOfInputData

from ui.ui_service import ConsoleUI

from config import DATA_FILE_PATH


def main():
    formatter = JsonFormatter()

    repository = JsonRepository(DATA_FILE_PATH, formatter)

    sorter = TransactionSorter()

    service = TransactionService(repository, sorter)

    validator = ValidatorOfInputData()

    ui = ConsoleUI(service, validator)

    ui.run()


if __name__ == "__main__":
    main()

