### Модуль с фикстурами

import pytest

from MyManager.core.entities import StructDataOfTransaction

from MyManager.infrastructure.data_manager import JsonRepository, JsonFormatter


@pytest.fixture
def json_repo(tmp_path):
    return JsonRepository(tmp_path / "expenses.json", JsonFormatter())

@pytest.fixture
def sample_transactions_list():

    return [
        StructDataOfTransaction(id=1, date="01.01.2024", amount=100.0,
                                typeOp="income",  description="зарплата"),
        StructDataOfTransaction(id=2, date="02.01.2024", amount=50.5,
                                typeOp="expense", description="кофе"),
        StructDataOfTransaction(id=3, date="02.01.2024", amount=550.0,
                                typeOp="expense", description="Стрижка в парикмахерской"),
    ]

@pytest.fixture
def sample_transactions_dict():

    return {
            "transactions": [
                {
                    "id": 1,
                    "date": "01.01.2024",
                    "amount": 100.0,
                    "typeOp": "income",
                    "description": "зарплата"
                },
                {
                   "id": 2,
                    "date": "02.01.2024",
                    "amount": 50.5,
                    "typeOp": "expense",
                    "description": "кофе" 
                },
                {
                    "id": 3,
                    "date": "02.01.2024",
                    "amount": 550.0,
                    "typeOp": "expense",
                    "description": "Стрижка в парикмахерской" 
                }
            ]
        }