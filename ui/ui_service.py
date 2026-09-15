### Вспомогательная логика UI

# Импорты

import sys
from services.data_service import TransactionReadService  # Зависим от конкретных реализаций !!!
from services.data_input_validator import ValidatorOfInputData  # Зависим от конкретных реализаций !!!


from .ui_output_data_modules.ui_output_custom_data import TransactionsOutputUI
from .ui_output_data_modules.ui_output_common_data import ConsoleInterfaceMessages

from .ui_layer_validator import UiValidatorOfInputData

from .ui_crud_methods import CRUDmenuMethods

# Конец импортов

########## РАЗДЕЛЮ КЛАССЫ ПО МОДУЛЯМ ##########

class RunApp:
    """Класс, реализующий методы по запуску потока приложения"""

    def __init__(self, general_ui: GeneralUiClass):
        self.general_ui = general_ui

    def run(self):
        """Вызов главного меню"""

        self.general_ui._stream_program()

class GeneralUiClass:  ## Переделать - нарушение SRP и переименовать
    """Главный ui-класс"""

    def __init__(self, read_service: TransactionReadService, validator: ValidatorOfInputData,
                 interfaces_menu: ConsoleInterfaceMessages, 
                 ui_level_validator: UiValidatorOfInputData, 
                 crud_menu_methods: CRUDmenuMethods, 
                 display_data_methods: TransactionsOutputUI):

        # Внешние зависимости (объекты классов других файлов)
        self.read_service = read_service
        self.validator = validator

        # Внутренние зависимости (объекты классов этого файла)
        self.interfaces_menu = interfaces_menu
        self.ui_level_validator = ui_level_validator
        self.crud_menu_methods = crud_menu_methods
        self.display_data_methods = display_data_methods

        # Переменная - словарь. Ключ - каждое главное меню, значение - словарь, в котором ключ - цифра, а значение - след. меню
        self._controller = {
            "_menu_main" : {
                1: self._menu_view,
                2: self._menu_edit,
                3: sys.exit
            },
            "_menu_view" : {
                1: self._action_view_direct,
                2: self._action_view_reversed,
                3: self._menu_sort,
                4: self._menu_main
            },
            "_menu_edit" : {
                1: self.crud_menu_methods._menu_add,
                2: self.crud_menu_methods._menu_change,
                3: self.crud_menu_methods._menu_delete,
                4: self._menu_main
            }
        }

    def _get_next_menu(self, name_of_current_menu: str, choosing_next_menu: int):
        """Метод, возвращающий след. меню для запуска в зависимости от выбора пользователя"""

        current_dict_with_one_name_and_choices = self._controller.get(name_of_current_menu)

        if current_dict_with_one_name_and_choices:
            return current_dict_with_one_name_and_choices.get(choosing_next_menu, f"Не найдено меню с выбором: {choosing_next_menu}")

        return f"Не найден метод меню с именем: {name_of_current_menu}"

    def _validate_type_of_current_menu(self, menu_method_for_validating):
        """Метод, проверяющий является ли тек. меню - главным, если да - true, если оно меню-опция, то - false"""

        if menu_method_for_validating in self._controller.keys():
            return True

        return False

    def _stream_program(self):
        """Метод, реализующий беск. цикл программы - безопасное переключение между методами"""

        current_menu = self._menu_main

        while True:
            next_choice = current_menu()

            if self._validate_type_of_current_menu(current_menu.__name__):  ## Если текущее меню - главное, то запоминаем его и идём к след. меню
                previos_menu = current_menu
                current_menu = self._get_next_menu(current_menu.__name__, next_choice)

            else:  ## Если нет - просто оставляем тек. меню
                current_menu = previos_menu

    def _action_view_direct(self):
        """Действие: Показ в прямом порядке"""

        data = self.read_service.get_all()

        self.display_data_methods._display_transactions(data)

    def _action_view_reversed(self):
        """Действие: Показ в прямом порядке"""

        data = self.read_service.get_all(reverse=True)
        
        self.display_data_methods._display_transactions(data)

    def _menu_main(self):
        """Функция вывода 1-го меню"""

        self.interfaces_menu._menu_main_interface()

        # Валидируем вводимое значение
        my_choice = self.ui_level_validator._get_validated_my_choice(1, 3)
        print()

        return my_choice

    def _menu_view(self):
        """Функция вывода 2-го меню со способами вывода информации"""

        self.interfaces_menu._menu_view_interface()

        # Валидируем вводимое значение
        my_choice = self.ui_level_validator._get_validated_my_choice(1, 4)
        print()

        return my_choice

    def _menu_edit(self):
        """Функция вывода меню с выбором изменения данных"""

        self.interfaces_menu._menu_edit_interface()

        # Валидируем вводимое значение
        my_choice = self.ui_level_validator._get_validated_my_choice(1, 4)
        print()

        return my_choice

    def _menu_sort(self):
        """Функция вывода отсортированного списка"""

        print("""Введите 1 цифру или последовательность цифр, 
    которые будут указывать сколько полей и в каком порядке отсортировать (Например,
    "1 4 3" означает, что сортируем по 1-му полю, если значения совпадают, то
    затем сортируем по 4-му полю, если и они совпадают, то по 3-му полю сортируем): """, end="\n\n")
        
        # Получаем номера полей от пользователя
        masForSorting = list(map(int, input().split()))
        print()

        if self.read_service.get_all() != []:
            result = self.read_service.get_sorted(masForSorting)

            self.display_data_methods._display_transactions(result)

        # Если файлик пуст, то не выполняем сортировку
        else:
            print("НЕТ ДАННЫХ В ФАЙЛЕ ДЛЯ СОРТИРОВКИ!!!")


