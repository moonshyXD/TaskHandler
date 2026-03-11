import pytest

from src.domain.descriptors import FilePathValidator, TaskCountValidator
from src.domain.errors import InputValidationError


class TestDescriptorContainer:
    count = TaskCountValidator()
    path = FilePathValidator()


class TestValidators:
    def test_count_validator(self) -> None:
        container = TestDescriptorContainer()

        container.count = "5"
        assert container.count == 5
        container.count = 10
        assert container.count == 10

        with pytest.raises(InputValidationError):
            container.count = "abc"

        with pytest.raises(InputValidationError):
            container.count = "-1"

    def test_file_path_validator(self, tmp_path: str) -> None:
        f = tmp_path / "test_file.txt"
        f.touch()

        container = TestDescriptorContainer()

        container.path = str(f)
        assert str(container.path) == str(f.resolve())

        with pytest.raises(InputValidationError):
            container.path = 123

        with pytest.raises(InputValidationError):
            container.path = "non_existent_file.txt"

        with pytest.raises(InputValidationError):
            container.path = str(tmp_path)
