## Файл с логикой действий проекта

## Описываем структуру полей данных
class StructDataOfTransactions:

    # Поля структуры (класса)

    IdTransaction = None  # Уникальный ID транзакции
    Date = None  # Дата транзакции
    Amount = 0  # Сумма транзакции
    TypeOfOperation = None  # Тип операции - доход/расход
    Description = ""  # Заметка об операции

    #  Инициализатор
    def __init__(self, date, amount, typeOfOperation, description):
        self.Date = date
        self.Amount = amount
        self.TypeOfOperation = typeOfOperation
        self.Description = description

    
    