# Главный файл, где собираем и запускаем сборку проекта (Точка входа)

from MyManager.ui.ui_service import ExitApp

from MyManager.composition_build import build

from MyManager.config import DATA_FILE_PATH


def main():
    """Главная Функция, где получаем собранные зависимости и запускаем ui - интерфейс"""

    
    execute_app = build(data_file_path=DATA_FILE_PATH)

    try:
        execute_app.stream_program()

    except ExitApp:
        pass


if __name__ == "__main__":
    main()

