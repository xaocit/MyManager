### Модуль с фикстурами

import pytest

from MyManager.services.data_service import (TransactionReadService,
                                             TransactionWriteService,
                                             TransactionCreatorOfNewId,
                                             TransactionSorter)


@pytest.fixture
def read_service_with_bd(json_repo, sample_transactions_list):
    json_repo.save_all(sample_transactions_list)
    return TransactionReadService(json_repo, TransactionSorter())

@pytest.fixture
def read_service_without_bd(json_repo):
    json_repo.save_all([])
    return TransactionReadService(json_repo, TransactionSorter())

@pytest.fixture
def write_service_with_bd(json_repo, read_service_with_bd, sample_transactions_list):
    json_repo.save_all(sample_transactions_list)
    return TransactionWriteService(json_repo, TransactionCreatorOfNewId(), read_service_with_bd)

@pytest.fixture
def write_service_without_bd(json_repo, read_service_without_bd):
    json_repo.save_all([])
    return TransactionWriteService(json_repo, TransactionCreatorOfNewId(), read_service_without_bd)
