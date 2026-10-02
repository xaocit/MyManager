# Тесты для методов сериализатора

from MyManager.infrastructure.data_manager import JsonFormatter


def test_formatter_from_dict(sample_transactions_list: list, sample_transactions_dict: dict):

    got = JsonFormatter().from_dict(sample_transactions_dict)
    assert sample_transactions_list == got

def test_formatter_to_dict(sample_transactions_list: list, sample_transactions_dict: dict):

    got = JsonFormatter().to_dict(sample_transactions_list)
    assert sample_transactions_dict == got