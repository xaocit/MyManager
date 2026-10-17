### Тесты для сервиса-чтения транзакций

import pytest
from datetime import datetime

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

        KEYS = {
            1: lambda t: datetime.strptime(t.date, "%d.%m.%Y"),
            2: lambda t: t.amount,
            3: lambda t: t.typeOp,
        }

        @pytest.mark.parametrize("fields", [
            [1], 
            [2],
            [1, 2],
            [3, 1],
            [3, 2, 1]
        ])
        def test_sorted_matches_reference(self, read_service_with_bd, sample_transactions_list, fields):

            expected = sorted(sample_transactions_list, key=lambda t: tuple(self.KEYS[item](t) for item in fields))

            assert [t.id for t in read_service_with_bd.get_sorted(fields)] == [t.id for t in expected]


    class TestFuncGetById:
        def test_get_by_exist_id(self, read_service_with_bd):

            got_index_of_data = read_service_with_bd.get_data_by_id(1)[0]

            assert got_index_of_data == True

        def test_get_by_non_existent_id(self, read_service_without_bd):
        
            got_index_of_data = read_service_without_bd.get_data_by_id(5)[0]

            assert got_index_of_data == False
