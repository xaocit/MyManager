# Тесты для методов сервисов


### Тесты для сервиса-чтения транзакций

def test_get_all(read_service, sample_transactions_list):
    
    got = read_service.get_all()
    assert got == sample_transactions_list

def test_get_by_id(read_service):

    got_index_of_data = read_service.get_data_by_id(1)[1]

    assert got_index_of_data == 0