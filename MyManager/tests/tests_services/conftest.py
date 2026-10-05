### Модуль с фикстурами

import pytest

from MyManager.services.data_service import (TransactionReadService,
                                             TransactionSorter)


@pytest.fixture
def read_service(json_repo, sample_transactions_list):
    json_repo.save_all(sample_transactions_list)
    return TransactionReadService(json_repo, TransactionSorter())

