### Вспомогательная логика UI

# Импорты

import sys
from services.data_service import TransactionService
from services.data_input_validator import ValidatorOfInputData

# Конец импортов

class ConsoleUI:
    """Класс с менюшками и методами, предназначенными для их работы"""

    def __init__(self, service: TransactionService, validator: ValidatorOfInputData):
        self.service = service

        self.validator = validator

########  ОБЫЧНЫЕ МЕТОДЫ МЕНЮ  ########

    def _menu_main(self):
        """Функция вывода 1-го меню"""

        print("Здравствуйте! Вы в менеджере ваших расходов и доходов. Что вы хотите сделать?", end="\n\n")

        print()

        print("Посмотреть данные - 1")
        print("Изменить данные - 2")
        print("Выйти - 3", end="\n\n")

        # Валидируем вводимое значение
        myChoice1 = self._get_validated_my_choice(1, 3)
        print()

        match myChoice1:

            case 1:
                self._menu_view()
            case 2:
                self._menu_edit()
            case 3:
                sys.exit()

    def _menu_view(self):
        """Функция вывода 2-го меню со способами вывода информации"""
        print()

        print()

        print("Посмотреть данные в прямом порядке - 1")
        print("Посмотреть данные в обратном порядке - 2")
        print("Посмотреть данные в отсортированном порядке - 3")
        print("Выйти - 4", end="\n\n")

        # Валидируем вводимое значение
        myChoice2 = self._get_validated_my_choice(1, 4)
        print()

        match myChoice2:

            case 1:
                self._display_transactions(self.service.get_all())
                self._menu_view()
            case 2:
                self._display_transactions(self.service.get_all(reverse=True))
                self._menu_view()
            case 3:
                self._menu_sort()
                self._menu_view()
            case 4:
                self._menu_main()

    def _menu_edit(self):
        """Функция вывода меню с выбором изменения данных"""

        print()

        print()

        print("Добавить новую запись в бд - 1")
        print("Изменить существующую запись в бд - 2")
        print("Удалить запись из бд - 3")
        print("Выйти - 4", end="\n\n")

        # Валидируем вводимое значение
        myChoice3 = self._get_validated_my_choice(1, 4)
        print()

        match myChoice3:

            case 1:
                self._menu_add()
                self._menu_edit()
            case 2:
                self._menu_change()
                self._menu_edit()
            case 3:
                #self._menu_delete(data)
                self._menu_edit()
            case 4:
                self._menu_main()

    def _menu_sort(self):
        """Функция вывода отсортированного списка"""

        print("""Введите 1 цифру или последовательность цифр, 
    которые будут указывать сколько полей и в каком порядке отсортировать (Например,
    "1 4 3" означает, что сортируем по 1-му полю, если значения совпадают, то
    затем сортируем по 4-му полю, если и они совпадают, то по 3-му полю сортируем): """, end="\n\n")
        
        # Получаем номера полей от пользователя
        masForSorting = list(map(int, input().split()))
        print()

        if self.service.get_all() != []:
            result = self.service.get_sorted(masForSorting)

            self._display_transactions(result)

        # Если файлик пуст, то не выполняем сортировку
        else:
            print("НЕТ ДАННЫХ В ФАЙЛЕ ДЛЯ СОРТИРОВКИ!!!")

########  МЕТОДЫ CRUD-МЕНЮ  ########

    def _menu_add(self):
        """Функция запроса данных у пользователя для добавления"""

        print()
        print()

        tuple_of_new_data = self._data_entry_logic()

        add_date, add_amount, add_type, add_description = tuple_of_new_data

        self.service.add(add_date, add_amount, add_type, add_description)

    def _menu_change(self):
        """Функция запроса данных у пользователя для изменения существующей записи в бд"""

        print(end="\n\n\n")

        # Получаем корректный id
        id_find = self._get_validated_id("Введите id записи, которую хотите изменить: ")

        print()

        # Получаем корректные данные, если они прошли проверки
        tuple_of_new_data = self._data_entry_logic()
        
        changed_date, changed_amount, changed_type, changed_description = tuple_of_new_data

        # Меняем в списке 1 элемент
        self.service.change_data(
            id_find, 
            changed_date, 
            changed_amount, 
            changed_type, 
            changed_description
            )



########  ВСПОМОГАТЕЛЬНЫЕ UI-МЕТОДЫ  ########

    def _display_transactions(self, list_for_display):
        """Функция красивого вывода данных в прямом или обратном порядке"""

        # Красивый вывод в виде таблицы
        print("-" * 80)
        print(f"{'ID':<5} {'Дата':<12} {'Сумма':<10} {'Тип':<15} {'Описание'}")
        print("-" * 80)
        for item in list_for_display:
            print(f"{item.id:<5} {item.date:<12} {float(item.amount):<10.2f} {item.typeOp:<15} {item.description}")
        print("-" * 80)

    def _data_entry_logic(self):
        """Метод, реализующий логику вывода ошибок, если они есть при добавлении или изменении записи
        Возвращает введённые данные, если они прошли проверки"""

        print()
        print("Введите строку с новыми данными через пробелы (например: 24.05.2024 600 income Вознаграждение за мойку посуды): ")

        while True:

            my_new_data_in_bd = input()
            
            # Отлавливаем ошибки, если валидация прошла неуспешно
            result_validate = self.validator.is_correct_input(my_new_data_in_bd, 4)

            # list - если ошибки связаны с неверным форматом полей
            # str - если возникла ошибка с количеством
            if isinstance(result_validate, str):
                print()
                print(f"Найдена ошибка в вводе: {result_validate}", end="\n\n")
                print("Попробуйте ещё раз ввести строку: ", end="\n\n")
            else:
                break

        print()

        new_date, new_amount, new_type, new_description = my_new_data_in_bd.split(None, 3)
        return (new_date, new_amount, new_type, new_description)

    def _get_validated_id(self, prompt):
        """Метод валидации вводимого id при изменении, удалении записи.
        Если всё успешно - возвращает введённый id"""

        while True:

            print(prompt)
            
            try: 
                id_find = int(input())

                if id_find < 0:
                    print()
                    print("Id должен быть больше нуля !!!", end="\n\n")
                    continue

                # Берём только 0-й индекс, поскольку нам нужно только bool - значение
                if not (self.service.get_data_by_id(id_find)[0]):
                    print()
                    print(f"Запись с {id_find} не найдена в базе !!!", end="\n\n")

                else:
                    return id_find

            except ValueError:
                print()
                print("Id должен быть числом !!!")

    def _get_validated_my_choice(self, min_value: int, max_value: int):
        """Метод для валидации выбора пользователя в различных меню"""

        while True:

            try:
                user_choice = int(input("Сделайте выбор: "))

                if min_value <= user_choice <= max_value:
                    return user_choice

                else:
                    print()
                    print(f"Введите значение с {min_value} до {max_value} !!!", end="\n\n")
                    continue

            except ValueError:
                print()
                print("Введите число !!!", end="\n\n")

    def run(self):
        """Вызов главного меню"""
        self._menu_main()