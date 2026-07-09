
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
            ...
        case 2:
            ...
        case 3:
            ...
        case _:
            print("Попробуйте ещё раз!!!", end="\n\n")
