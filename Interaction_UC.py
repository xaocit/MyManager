import sys


## Функция вывода 1-го меню
def Menu1():
    
    print("Здравствуйте! Вы в менеджере ваших расходов и доходов. Что вы хотите сделать?", end="\n\n")

    print()

    print("Посмотреть данные - 1")
    print("Изменить данные - 2")
    print("Выйти - 3", end="\n\n")

    myChoice1 = int(input("Сделайте выбор: "))
    print()

    match myChoice1:

        case 1:
            Menu2()
        case 2:
            ...
        case 3:
            sys.exit()
        case _:
            print("Попробуйте ещё раз!!!", end="\n\n")



## Функция вывода 2-го меню со способами вывода информации
def Menu2():
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
            ...
        case 2:
            ...
        case 3:
            sys.exit()
        case _:
            print("Попробуйте ещё раз!!!", end="\n\n")