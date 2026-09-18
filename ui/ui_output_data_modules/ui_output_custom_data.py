### Модуль с логикой вывода списка транзакций (и любых кастомных данных) в консоль


class TransactionsOutputUI:
    """Класс, реализующий методы по выводу данных в интерфейс ui"""

    def _display_transactions(self, list_for_display):
        """Функция красивого вывода данных в прямом или обратном порядке"""

        print("-" * 80)
        print(f"{'ID':<5} {'Дата':<12} {'Сумма':<10} {'Тип':<15} {'Описание'}")
        print("-" * 80)
        for item in list_for_display:
            print(f"{item.id:<5} {item.date:<12} {float(item.amount):<10.2f} {item.typeOp:<15} {item.description}")
        print("-" * 80)