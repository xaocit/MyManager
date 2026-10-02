# Тесты для методов репозитория


def test_load_all_returns_empty_when_file_missing(json_repo):
    assert json_repo.load_all() == []

def test_save_all_and_then_load_all(json_repo, sample_transactions_list):
    json_repo.save_all(sample_transactions_list)
    assert json_repo.load_all() == sample_transactions_list