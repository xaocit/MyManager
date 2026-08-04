# Вспомогательная логика UI

import sys
from services.data_service import TransactionService


class ConsoleUI:

    def __init__(self, service: TransactionService):
        self.service = service


    ## Функция вывода 1-го меню
    def _menu_main(self, data):

        print("Здравствуйте! Вы в менеджере ваших расходов и доходов. Что вы хотите сделать?", end="\n\n")

        print()

        print("Посмотреть данные - 1")
        print("Изменить данные - 2")
        print("Выйти - 3", end="\n\n")

        myChoice1 = int(input("Сделайте выбор: "))
        print()

        match myChoice1:

            case 1:
                self._menu_view(data)
            case 2:
                self._menu_edit(data)
            case 3:
                sys.exit()
            case _:
                print("Попробуйте ещё раз!!!", end="\n\n")
                self._menu_main(data)



    ## Функция вывода 2-го меню со способами вывода информации
    def _menu_view(self, data):
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
                self._display_transactions(data, 1)
                self._menu_view(data)
            case 2:
                self._display_transactions(data, -1)
                self._menu_view(data)
            case 3:
                self._menu_sort()
                self._menu_view(data)
            case 4:
                self._menu_main(data)
            case _:
                print("Попробуйте ещё раз!!!", end="\n\n")
                self._menu_view(data)

    ## Функция вывода меню с выбором изменения данных
    def _menu_edit(self, data):

        print()

        print()

        print("Добавить новую запись в бд - 1")
        print("Изменить существующую запись в бд - 2")
        print("Удалить запись из бд - 3")
        print("Выйти - 4", end="\n\n")

        myChoice3 = int(input("Сделайте выбор: "))
        print()

        match myChoice3:

            case 1:
                self._menu_add()
                self._menu_edit(data)
            case 2:
                #self._menu_update(data)
                self._menu_edit(data)
            case 3:
                #self._menu_delete(data)
                self._menu_edit(data)
            case 4:
                self._menu_main(data)
            case _:
                print("Попробуйте ещё раз!!!", end="\n\n")
                self._menu_edit(data)

    ## Функция красивого вывода данных в прямом или обратном порядке
    def _display_transactions(self, data, mode):

        # Красивый вывод в виде таблицы
        print("-" * 80)
        print(f"{'ID':<5} {'Дата':<12} {'Сумма':<10} {'Тип':<15} {'Описание'}")
        print("-" * 80)
        for item in self.service._transactions[::mode]:
            print(f"{item.id:<5} {item.date:<12} {float(item.amount):<10.2f} {item.typeOp:<15} {item.description}")
        print("-" * 80)


    ## Функция вывода отсортированного списка
    def _menu_sort(self):

        print("""Введите 1 цифру или последовательность цифр, 
    которые будут указывать сколько полей и в каком порядке отсортировать (Например,
    "1 4 3" означает, что сортируем по 1-му полю, если значения совпадают, то
    затем сортируем по 4-му полю, если и они совпадают, то по 3-му полю сортируем): """, end="\n\n")
        
        # Получаем номера полей от пользователя
        masForSorting = list(map(int, input().split()))
        print()

        if self.service._transactions != []:
            result = self.service.get_sorted(masForSorting)

            self._display_transactions(result, 1)

        # Если файлик пуст, то не выполняем сортировку
        else:
            print("НЕТ ДАННЫХ В ФАЙЛЕ ДЛЯ СОРТИРОВКИ!!!")

    ## Функция запроса данных у пользователя для добавления
    def _menu_add(self):

        print()
        print()

        print("Введите строку с новыми данными через пробелы (например: 24.05.2024 600 income Вознаграждение за мойку посуды): ")

        print()

        myNewDataInBD = input().split(None, 3)
        print()

        self.service.add(myNewDataInBD[0], myNewDataInBD[1], myNewDataInBD[2], myNewDataInBD[3])


    # Вызов главного меню
    def run(self):
        self._menu_main(self.service.get_all())