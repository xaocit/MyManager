# Тесты для методов сериализатора

from ...infrastructure.data_manager import JsonFormatter


def test_formatter_from_dict(sample_transactions_list: list, sample_transactions_dict: dict):

    got = JsonFormatter().from_dict(sample_transactions_dict)
    assert sample_transactions_list == got