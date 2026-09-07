### Файл с утилитами для функций бд (сервисы)

from typing import List, Union

from core.entities import StructDataOfTransaction
from core.interfaces import IRepository, ISorter, ICreatorOfNewId


class FactoryTransactionDependencies:
    """Класс, реализующий сборку зависимостей для классов Transaction<Read/Write>Service"""

    def __init__(self, repository: IRepository, creator_of_new_id: ICreatorOfNewId, sorter: List[ISorter] = None):

        self._repository = repository
        self._creator_of_new_id = creator_of_new_id
        self._sorter = sorter

    def get_read_service(self):
        return TransactionReadService(repository=self._repository, sorter=self._sorter)

    def get_write_service(self):

        read_service = self.get_read_service()

        return TransactionWriteService(repository=self._repository, creator_of_new_id=self._creator_of_new_id,
                                       read_service=read_service)



class TransactionReadService:
    """Класс, реализующий методы для чтения данных из списка транзакций в разных вариациях"""

    def __init__(self, repository: IRepository, sorter: List[ISorter] = None):

        self.repository = repository
        self.sorter = sorter

    def get_all(self, reverse=False) -> List[StructDataOfTransaction]:
        """Публичный метод-геттер для доступа к копии списка транзакций (прямого или обратного)"""

        transactions = self.repository.load_all()

        is_reverse_int = int(reverse)

        return transactions.copy()[::-1 if is_reverse_int == 1 else 1]

    def get_sorted(self, field_indicies: List[int]) -> List[StructDataOfTransaction]:
        """Публичный метод-геттер для доступа к отсортированному списку транзакций"""

        transactions = self.repository.load_all()

        # Если self.sorter имеется, то возвращаем отсортированный список
        if not (self.sorter is None):
            return self.sorter.my_sort(transactions, field_indicies)

        # Иначе возвращаем просто список транзакций
        return transactions

    def get_data_by_id(self, find_id: int) -> tuple[bool, Union[int | None]]:
        """Метод, возвращающий кортеж, в котором 1-й элемент bool-значение:
        т. е. есть ли запись с find_id или нет; 
        а 2-й элемент - индекс найденной записи или None, если не нашли"""

        transactions = self.repository.load_all()

        # Перебираем в цикле каждую транзакцию, ища нужную
        for i, transaction in enumerate(transactions):
            if find_id == transaction.id:
                return (True, i)

        return (False, None)


class TransactionWriteService:
    """Класс, реализующий методы для изменения данных (CUD) в списке транзакций"""

    def __init__(self, repository: IRepository, creator_of_new_id: ICreatorOfNewId,
                 read_service: TransactionReadService
                 ):

        self.read_service = read_service

        self.repository = repository
        self.creator_of_new_id = creator_of_new_id

    def add(self, new_date, new_amount, new_type_op, new_description) -> StructDataOfTransaction:
        """Логика добавления новой записи в бд"""

        transactions = self.repository.load_all()

        # Определяем id для новой записи
        new_id = self.creator_of_new_id.create_new_id(transactions)

        new_Transaction = StructDataOfTransaction(
            id=new_id,
            date=new_date,
            amount=new_amount,
            typeOp=new_type_op,
            description=new_description
        )

        transactions.append(new_Transaction)

        self.repository.save_all(transactions)

        return new_Transaction

    def change_data(self, find_id, changed_date, changed_amount, changed_type_op, changed_description):
        """Метод, позволяющий изменить существующую строку в бд"""

        # Используем метод get_data_by_id из этого же класса для
        # получение индекса найденной записи, чтобы по нему заменить данные
        
        transactions = self.repository.load_all()

        index_for_changing = self.read_service.get_data_by_id(find_id)[1]

        transactions[index_for_changing] = StructDataOfTransaction(
            id=find_id,
            date=changed_date,
            amount=changed_amount,
            typeOp=changed_type_op,
            description=changed_description
        )

        # Сохраняем в файле
        self.repository.save_all(transactions)

    def delete_data(self, find_id):
        """Метод, удаляющий запись в бд по id"""

        transactions = self.repository.load_all()

        index_for_deleting = self.read_service.get_data_by_id(find_id)[1]

        # Удаляем транзакцию по id
        del transactions[index_for_deleting]

        # Сохраняем в файл
        self.repository.save_all(transactions)


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