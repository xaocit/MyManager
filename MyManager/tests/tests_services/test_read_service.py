### Тесты для сервиса-чтения транзакций


from MyManager.core.entities import StructDataOfTransaction


class TestReadService:

    class TestFuncGetAll:
        def test_get_all_ordinary(self, read_service_with_bd, sample_transactions_list):
            
            got = read_service_with_bd.get_all()
            assert got == sample_transactions_list

        def test_get_all_reversed(self, read_service_with_bd, sample_transactions_list):
                    
            got = read_service_with_bd.get_all(True)
            assert got == sample_transactions_list[::-1]


    class TestFuncGetSorted:
        def test_get_sorted_amount(self, read_service_with_bd):

            got_sorted_data = read_service_with_bd.get_sorted([1])

            assert got_sorted_data == [
        StructDataOfTransaction(id=2, date="02.01.2024", amount=50.5,
                                typeOp="expense", description="кофе"),
        StructDataOfTransaction(id=1, date="01.01.2024", amount=100.0,
                                typeOp="income",  description="зарплата"),
        StructDataOfTransaction(id=3, date="02.01.2024", amount=550,
                                typeOp="expense", description="Стрижка в парикмахерской"),
    ]
            
        def test_get_sorted_date_and_amount(self, read_service_with_bd):
        
            got_sorted_data = read_service_with_bd.get_sorted([0, 1])

            assert got_sorted_data == [
        StructDataOfTransaction(id=1, date="01.01.2024", amount=100.0,
                                typeOp="income",  description="зарплата"),
        StructDataOfTransaction(id=2, date="02.01.2024", amount=50.5,
                                typeOp="expense", description="кофе"),
        StructDataOfTransaction(id=3, date="02.01.2024", amount=550,
                                typeOp="expense", description="Стрижка в парикмахерской"),
    ]
            
        def test_get_sorted_typeOp_and_amount(self, read_service_with_bd):
                
            got_sorted_data = read_service_with_bd.get_sorted([2, 1])

            assert got_sorted_data == [
        StructDataOfTransaction(id=2, date="02.01.2024", amount=50.5,
                                typeOp="expense", description="кофе"),
        StructDataOfTransaction(id=3, date="02.01.2024", amount=550,
                                typeOp="expense", description="Стрижка в парикмахерской"),
        StructDataOfTransaction(id=1, date="01.01.2024", amount=100.0,
                                typeOp="income",  description="зарплата"),
    ]


    class TestFuncGetById:
        def test_get_by_exist_id(self, read_service_with_bd):

            got_index_of_data = read_service_with_bd.get_data_by_id(1)[0]

            assert got_index_of_data == True

        def test_get_by_non_existent_id(self, read_service_without_bd):
        
            got_index_of_data = read_service_without_bd.get_data_by_id(5)[0]

            assert got_index_of_data == False
