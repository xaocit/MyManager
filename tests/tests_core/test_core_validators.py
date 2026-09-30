# Тесты для методов валидации в ядре

import pytest

from ...core.core_validators import (ValidateId,
                                  ValidateDate,
                                  ValidateAmount,
                                  ValidateTypeOfOperation)

@pytest.mark.parametrize(
    ("id", "expected"),
    [
        ("5", True),
        ("0", True),
        ("ab3", "Ошибка! Id должен быть числом !!!"),
    ],
    ids=["valid_5", "valid_0", "not_a_number"],
)
def test_is_correct_id(id: str, expected: str | bool) -> None:

    got = ValidateId.is_correct_id(id)

    assert expected == got
