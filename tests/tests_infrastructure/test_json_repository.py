# Тесты для методов репозитория

import pytest

from ...infrastructure.data_manager import (JsonRepository, 
                                            JsonFormatter)


def test_load_all_returns_empty_when_file_missing(json_repo):
    assert json_repo.load_all() == []
