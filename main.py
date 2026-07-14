###### ГЛАВНЫЙ ФАЙЛ ПРОЕКТА - ТОЧКА ВХОДА.


### Импорты файлов
import Interaction_UC
import DataManager


if __name__ == "__main__":

    dataBase = DataManager.readingDataFromFile()  # Читаем базу данных на старте и сохраняем в переменную

    while True:
        Interaction_UC.Menu1()