from typing import Any

import pytest

from src.adapters.validators import FilePathValidator, TaskCountValidator
from src.domain.errors import InputValidationError


class Descriptors:
    count = TaskCountValidator()
    path = FilePathValidator()


class TestValidators:
    def test_count_valid(self) -> None:
        d = Descriptors()
        d.count = "5"
        assert d.count == 5

    def test_count_invalid(self) -> None:
        with pytest.raises(InputValidationError):
            Descriptors().count = "abc"
        with pytest.raises(InputValidationError):
            Descriptors().count = "-1"

    def test_path_valid(self, tmp_path: Any) -> None:
        f = tmp_path / "test.txt"
        f.touch()
        d = Descriptors()
        d.path = str(f)
        assert str(d.path).endswith("test.txt")

    def test_path_invalid(self, tmp_path: Any) -> None:
        with pytest.raises(InputValidationError):
            Descriptors().path = 123
        with pytest.raises(InputValidationError):
            Descriptors().path = "goose.txt"
        with pytest.raises(InputValidationError):
            Descriptors().path = str(tmp_path)
