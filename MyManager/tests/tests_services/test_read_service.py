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

            got_sorted_data = read_service_with_bd.get_sorted([2])

            got_sorted_data_ids = []
            for transaction in got_sorted_data:
                got_sorted_data_ids.append(transaction.id)

            assert [2, 1, 3] == got_sorted_data_ids
            
        def test_get_sorted_date_and_amount(self, read_service_with_bd):
        
            got_sorted_data = read_service_with_bd.get_sorted([1, 2])

            got_sorted_data_ids = []
            for transaction in got_sorted_data:
                got_sorted_data_ids.append(transaction.id)

            assert [1, 2, 3] == got_sorted_data_ids
            
        def test_get_sorted_typeOp_and_amount(self, read_service_with_bd):
                
            got_sorted_data = read_service_with_bd.get_sorted([3, 2])

            got_sorted_data_ids = []
            for transaction in got_sorted_data:
                got_sorted_data_ids.append(transaction.id)

            assert [2, 3, 1] == got_sorted_data_ids


    class TestFuncGetById:
        def test_get_by_exist_id(self, read_service_with_bd):

            got_index_of_data = read_service_with_bd.get_data_by_id(1)[0]

            assert got_index_of_data == True

        def test_get_by_non_existent_id(self, read_service_without_bd):
        
            got_index_of_data = read_service_without_bd.get_data_by_id(5)[0]

            assert got_index_of_data == False
