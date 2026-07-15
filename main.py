######
###### ГЛАВНЫЙ ФАЙЛ ПРОЕКТА - ТОЧКА ВХОДА.
######


### Импорты файлов
import Interaction_UC
import DataManager
import myStructs


if __name__ == "__main__":

    # Читаем базу данных и соханяем её перед использованием в программе
    dataBase = DataManager.readingDataFromFile()  

    ## Формируем список записей данных для удобства
    listOfDataBase = [myStructs.StructDataOfTransactions(i["id"], i["date"], i["amount"], i["type"], i["description"]) for i in dataBase["transactions"]]

    # Запускаем главное меню для начала работы программы
    Interaction_UC.Menu1_1(listOfDataBase)