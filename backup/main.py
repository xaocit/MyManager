######
###### ГЛАВНЫЙ ФАЙЛ ПРОЕКТА - ТОЧКА ВХОДА.
######


### Импорты файлов
import backup.Interaction_UC as Interaction_UC
import backup.DataManager as DataManager
import backup.myStructs as myStructs
import backup.myServices as myServices


if __name__ == "__main__":

    # Читаем базу данных и соханяем её перед использованием в программе
    dataBase = DataManager.readingDataFromFile()  

    # Вызываем функцию форматирвания данных из файлового формата словаря в список структур
    listOfDataBase = myServices.formateFromDbToList(dataBase)

    # Запускаем главное меню для начала работы программы
    Interaction_UC.Menu1_1(listOfDataBase)