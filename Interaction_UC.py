######
###### Файл взаимодействия пользователя с прогарммой через консоль 
######


import sys
import myServices

## Функция вывода 1-го меню
def Menu1_1(listOfDataBase):

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
            pprintData(listOfDataBase, 1)
            Menu1_2(listOfDataBase)
        case 2:
            pprintData(listOfDataBase, -1)
            Menu1_2(listOfDataBase)
        case 3:
            pprintSortedData(listOfDataBase)
            Menu1_2(listOfDataBase)
        case 4:
            sys.exit()
        case _:
            print("Попробуйте ещё раз!!!", end="\n\n")
            Menu1_2(listOfDataBase)


## Функция красивого вывода данных в прямом или обратном порядке
def pprintData(listOfDataBase, mode):

    # Красивый вывод в виде таблицы
    print("-" * 80)
    print(f"{'ID':<5} {'Дата':<12} {'Сумма':<10} {'Тип':<15} {'Описание'}")
    print("-" * 80)
    for item in listOfDataBase[::mode]:
        print(f"{item.IdTransaction:<5} {item.Date:<12} {item.Amount:<10.2f} {item.TypeOfOperation:<15} {item.Description}")
    print("-" * 80)


## Функция вывода отсортированного списка
def pprintSortedData(listOfDataBase):

    print("""Введите 1 цифру или последовательность цифр, 
которые будут указывать сколько полей и в каком порядке отсортировать (Например,
"1 4 3" означает, что сортируем по 1-му полю, если значения совпадают, то
затем сортируем по 4-му полю, если и они совпадают, то по 3-му полю сортируем): """, end="\n\n")
    
    # Получаем номера полей от пользователя
    masForSorting = list(map(int, input().split()))
    print()
    
    result = myServices.getSortedData(listOfDataBase, masForSorting)

    pprintData(result, 1)