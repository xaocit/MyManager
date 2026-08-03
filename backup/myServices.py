######
###### Файл с логикой действий проекта
######

import backup.myStructs as myStructs
import backup.DataManager as DataManager

# Функция получения отсортированного списка на основе 
# настроек критериев этой сортировки пользователем
def getSortedData(listOfDataBase, masForSorting):

    # Показываем доступные поля (атрибуты объекта)
    first_obj = listOfDataBase[0]

    # Получаем все атрибуты объекта (кроме служебных). 
    # dir() - возвращает все методы и поля объекта
    # getattr(obj, attr) - возвращает значение атрибута объекта по его имени (строке) 
    # callable(object) - проверяет, является ли объект вызываемым (функцией, методом, классом, объектом с методом __call__
    available_fields = [attr for attr in dir(first_obj) 
                       if not attr.startswith('__') and not callable(getattr(first_obj, attr))]
    
    # Преобразуем номера в имена полей
    fields_for_sorting = [available_fields[i-1] for i in masForSorting]
    
    # Создаем ключ для сортировки
    def makeSortKey(item):
        # Получаем значения выбранных полей в виде кортежа
        return tuple(getattr(item, field) for field in fields_for_sorting)
    
    return sorted(listOfDataBase, key=makeSortKey)


# Функция добавления новой записи в бд
def appendData(listOfDataBase, myNewData):

    newDate, newAmount, newTypeOfOperation, newDescription = (myNewData[i] for i in range(0, 4))

    listOfDataBase.append(myStructs.StructDataOfTransactions(5435, newDate, newAmount, newTypeOfOperation, newDescription))

    # Форматируем данные, переводя из вида списка в словарь, для последующей записи данных в файл
    dbFormatted = formateFromListToDb(listOfDataBase)

    # Перезаписываем данные в файлике
    DataManager.writeDataToFile(dbFormatted)


# Функция изменения записи в бд
def changeData(listOfDataBase, id, myNewData):

    ...


# Функция удаления записи из бд
def removeData(listOfDataBase, id):

    ...

# Функция переделывания из формата файла .jsonc в список структур
## Формируем список записей данных для удобства
def formateFromDbToList(dataBase):
    listOfDataBase = [myStructs.StructDataOfTransactions(i["id"], i["date"], i["amount"], i["type"], i["description"]) for i in dataBase["transactions"]]
    return listOfDataBase

# Функция переделывания из списка структур в формат файла .jsonc
## Формируем список записей данных для удобства
def formateFromListToDb(listOfDataBase):
    
    dataBase = {"transactions": []}

    for i in listOfDataBase:
        dataBase["transactions"].append(
            {
                "id": i.IdTransaction,
                "date": i.Date,
                "amount": i.Amount,
                "type": i.TypeOfOperation,
                "description": i.Description
            }
        )

    return dataBase