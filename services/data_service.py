### Файл с утилитами для функций бд (сервисы)

from core.entities import StructDataOfTransaction
from core.interfaces import IRepository, ISorter, ICreatorOfNewId

class TransactionService:
    """Класс-сервис, реализующий публичный интерфейс для работы со списком транзакций"""

    def __init__(self, repository: IRepository, creator_of_new_id: ICreatorOfNewId, sorter: List[ISorter] = None):
        self._transactions = repository.load_all()

        self.repository = repository
        self.creator_of_new_id = creator_of_new_id
        self.sorter = sorter

    def add(self, new_date, new_amount, new_type_op, new_description) -> StructDataOfTransaction:
        """Логика добавления новой записи в бд"""

        # Определяем id для новой записи
        new_id = self.creator_of_new_id.create_new_id(self._transactions)

        new_Transaction = StructDataOfTransaction(
            id=new_id,
            date=new_date,
            amount=new_amount,
            typeOp=new_type_op,
            description=new_description
        )

        self._transactions.append(new_Transaction)

        self.repository.save_all(self._transactions)

        return new_Transaction


    def get_all(self, reverse=False) -> List[StructDataOfTransaction]:
        """Публичный метод-геттер для доступа к копии списка транзакций (прямого или обратного)"""

        is_reverse_int = int(reverse)

        return self._transactions.copy()[::-1 if is_reverse_int == 1 else 1]


    def get_sorted(self, field_indicies: List[int]) -> List[StructDataOfTransaction]:
        """Публичный метод-геттер для доступа к отсортированному списку транзакций"""

        # Если self.sorter имеется, то возвращаем отсортированный список
        if not (self.sorter is None):
            return self.sorter.my_sort(self._transactions, field_indicies)

        # Иначе возвращаем просто список транзакций
        return self._transactions

class TransactionCreatorOfNewId(ICreatorOfNewId):
    """Класс, реализующий метод формирования id для новой записи"""

    def create_new_id(self, transactions: List[StructDataOfTransaction]) -> int:
        """Метод, возвращающий свободный id для новой записи"""

        max_exist_id = 0
        for i in transactions:
            max_exist_id = max(max_exist_id, i.id)

        new_id = max_exist_id + 1
        return new_id

class TransactionSorter(ISorter):
    """Класс, реализующий кастомную сортировку"""

    def my_sort(self, data, field_indicies):
        """Метод, возвращающий отсортированный список по заданным полям"""
    
        # Получаем все атрибуты объекта (кроме служебных). 
        # dir() - возвращает все методы и поля объекта
        # getattr(obj, attr) - возвращает значение атрибута объекта по его имени (строке) 
        # callable(object) - проверяет, является ли объект вызываемым (функцией, методом, классом, объектом с методом __call__
        available_fields = [attr for attr in dir(data[0]) 
                        if not attr.startswith('__') and not callable(getattr(data[0], attr))]
        
        # Преобразуем номера в имена полей
        fields_for_sorting = [available_fields[i-1] for i in field_indicies]
        
        # Создаем ключ для сортировки
        def makeSortKey(item):
            # Получаем значения выбранных полей в виде кортежа
            return tuple(getattr(item, field) for field in fields_for_sorting)
        
        return sorted(data, key=makeSortKey)