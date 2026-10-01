### Модуль с фикстурами

import pytest

from ...core.entities import StructDataOfTransaction

from ...infrastructure.data_manager import JsonRepository, JsonFormatter


@pytest.fixture
def json_repo(tmp_path):
    return JsonRepository(tmp_path / "expenses.json", JsonFormatter())


@pytest.fixture
def sample_transactions():

    return [
        StructDataOfTransaction(id="1", date="01.01.2024", amount=100.0,
                                typeOp="income",  description="зарплата"),
        StructDataOfTransaction(id="2", date="02.01.2024", amount=50.5,
                                typeOp="expense", description="кофе"),
    ]