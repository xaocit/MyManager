# Главный файл, где собираем и запускаем сборку проекта (Точка входа)

import sys

from MyManager.ui.ui_service import ExitApp

from MyManager.composition_build import build

from MyManager.config import DATA_FILE_PATH


def main():
    """Главная Функция, где получаем собранные зависимости и запускаем ui - интерфейс"""


    try:
        execute_app = build(data_file_path=DATA_FILE_PATH)
        execute_app.stream_program()

    except ExitApp:
        pass

    except Exception:
        print("Непредвиденная ошибка!!!")
        sys.exit()


if __name__ == "__main__":
    main()

