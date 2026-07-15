######
###### Файл с логикой действий проекта
######


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