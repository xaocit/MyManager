## Файл взаимодействия программы с данными в .json - файле

### Импорт модуля, необходимого для работы с .jsonc - файлами
import commentjson

# Функция чтения данных из файла .json при первом открытии
def readingDataFromFile():

    with open('MyDataBase.jsonc', 'r', encoding='utf-8') as file:

        data = commentjson.load(file)

        return data
    

# Функция записи данных в файл json. Получает на вход старые данные файла и новые
def writeDataToFile(data, newData):

    data["transactions"].append(newData)

    with open('MyDataBase.jsonc', 'w', encoding='utf-8') as file:
        commentjson.dump(data, file, indent=4, ensure_ascii=False)