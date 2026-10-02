# Тесты для методов валидации в ядре

import pytest

from ...core.core_validators import (ValidateId,
                                  ValidateDate,
                                  ValidateAmount,
                                  ValidateTypeOfOperation)

@pytest.mark.parametrize(
    ("new_id", "expected"),
    [
        ("5", True),
        ("0", True),
        ("ab3", "Ошибка! Id должен быть числом !!!"),
    ],
    ids=["valid_5", "valid_0", "not_a_number"],
)
def test_is_correct_id(new_id: str, expected: str | bool) -> None:

    got = ValidateId.is_correct_id(new_id)

    assert expected == got


@pytest.mark.parametrize(
    ("new_date", "expected"),
    [
        ("05.06.2021", True),
        ("01.10.2026", True),
        ("04.13.2022", "Ошибка! Неверный формат введённой даты или её не существует !!!"),
        ("04-12-2026", "Ошибка! Неверный формат введённой даты или её не существует !!!"),
        ("03-12-24", "Ошибка! Неверный формат введённой даты или её не существует !!!"),
        ("076-12-26", "Ошибка! Неверный формат введённой даты или её не существует !!!"),
    ],
)
def test_is_correct_date(new_date: str, expected: str | bool) -> None:

    got = ValidateDate.is_correct_date(new_date)

    assert expected == got


@pytest.mark.parametrize(
    ("new_amount", "expected"),
    [
        ("566.16", True),
        ("34$", "Ошибка! Сумма должна быть числом !!!"),
        ("178 rub", "Ошибка! Сумма должна быть числом !!!"),
        ("-967.5", "Ошибка! Сумма должна быть положительной !!!"),
    ],
)
def test_is_correct_amount(new_amount: str, expected: str | bool) -> None:

    got = ValidateAmount.is_correct_amount(new_amount)

    assert expected == got


@pytest.mark.parametrize(
    ("new_type_operation", "expected"),
    [
        ("expense", True),
        ("income", True),
        ("inc", "Ошибка! Тип операции должен быть 'expense' или 'income' !!!")
    ]
)
def test_is_correct_type_of_operation(new_type_operation: str, expected: str | bool) -> None:

    got = ValidateTypeOfOperation.is_correct_type_of_operation(new_type_operation)

    assert expected == got