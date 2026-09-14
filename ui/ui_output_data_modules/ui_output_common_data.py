### Модуль с выводами сообщений меню действий с кнопками


class ConsoleInterfaceMessages:
    """Класс с ui-интерфейсами различных меню"""

    @staticmethod
    def _menu_main_interface():

        print("Здравствуйте! Вы в менеджере ваших расходов и доходов. Что вы хотите сделать?", end="\n\n")
        
        print()

        print("Посмотреть данные - 1")
        print("Изменить данные - 2")
        print("Выйти - 3", end="\n\n")

    @staticmethod
    def _menu_view_interface():

        print()

        print()

        print("Посмотреть данные в прямом порядке - 1")
        print("Посмотреть данные в обратном порядке - 2")
        print("Посмотреть данные в отсортированном порядке - 3")
        print("Выйти - 4", end="\n\n")

    @staticmethod
    def _menu_edit_interface():

        print()
        
        print()

        print("Добавить новую запись в бд - 1")
        print("Изменить существующую запись в бд - 2")
        print("Удалить запись из бд - 3")
        print("Выйти - 4", end="\n\n")
