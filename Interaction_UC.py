import sys
import DataManager
import Tasks

## Функция вывода 1-го меню
def Menu1_1():

    # Читаем базу данных и соханяем её перед использованием в программе
    dataBase = DataManager.readingDataFromFile()  

    ## Формируем список записей данных для удобства
    listOfDataBase = [Tasks.StructDataOfTransactions(i["id"], i["date"], i["amount"], i["type"], i["description"]) for i in dataBase["transactions"]]

    print("Здравствуйте! Вы в менеджере ваших расходов и доходов. Что вы хотите сделать?", end="\n\n")

    print()

    print("Посмотреть данные - 1")
    print("Изменить данные - 2")
    print("Выйти - 3", end="\n\n")

    myChoice1 = int(input("Сделайте выбор: "))
    print()

    match myChoice1:

        case 1:
            Menu1_2(listOfDataBase)
        case 2:
            ...
        case 3:
            sys.exit()
        case _:
            print("Попробуйте ещё раз!!!", end="\n\n")
            Menu1_1()



## Функция вывода 2-го меню со способами вывода информации
def Menu1_2(listOfDataBase):
    print()

    print()

    print("Посмотреть данные в прямом порядке - 1")
    print("Посмотреть данные в обратном порядке - 2")
    print("Посмотреть данные в отсортированном порядке - 3")
    print("Выйти - 4", end="\n\n")

    myChoice2 = int(input("Сделайте выбор: "))
    print()

    match myChoice2:

        case 1:
            pprintDataForward(listOfDataBase, 1)
            Menu1_2(listOfDataBase)
        case 2:
            pprintDataForward(listOfDataBase, -1)
            Menu1_2(listOfDataBase)
        case 3:
            ...
        case 4:
            sys.exit()
        case _:
            print("Попробуйте ещё раз!!!", end="\n\n")
            Menu1_2(listOfDataBase)


## Функция красивого вывода данных в прямом или обратном порядке
def pprintDataForward(listOfDataBase, mode):

    # Красивый вывод в виде таблицы
    print("-" * 80)
    print(f"{'ID':<5} {'Дата':<12} {'Сумма':<10} {'Тип':<15} {'Описание'}")
    print("-" * 80)
    for item in listOfDataBase[::mode]:
        print(f"{item.IdTransaction:<5} {item.Date:<12} {item.Amount:<10.2f} {item.TypeOfOperation:<15} {item.Description}")
    print("-" * 80)

