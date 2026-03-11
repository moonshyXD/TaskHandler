from datetime import timedelta

import pytest

from src.domain.errors import InputValidationError
from src.domain.task import Task


class TestDomain:
    def test_task_creation_valid(self) -> None:
        task = Task(description="Valid task", priority=3, status=0, id=100)
        assert task.id == 100
        assert task.description == "Valid task"
        assert task.priority == 3
        assert task.status == 0
        assert isinstance(task.task_duration, timedelta)

    def test_description_validation(self) -> None:
        with pytest.raises(InputValidationError):
            Task(description="", priority=3, status=0)

        with pytest.raises(InputValidationError):
            Task(description=123, priority=3, status=0)

        long_desc = "GOOOOOOOSEEEEEEEEEE"
        task = Task(description=long_desc, priority=3, status=0)
        assert task.short_description == "GOOOOOOOSE..."
        assert len(task.short_description) == 13

    def test_priority_validation(self) -> None:
        with pytest.raises(InputValidationError):
            Task(description="Task", priority="high", status=0)

        with pytest.raises(InputValidationError):
            Task(description="Task", priority=0, status=0)

        with pytest.raises(InputValidationError):
            Task(description="Task", priority=6, status=0)

    def test_status_validation(self) -> None:
        task = Task(description="Task", priority=3, status=1)
        assert task.status == 1

        with pytest.raises(ValueError):
            Task(description="Task", priority=3, status=2)

        with pytest.raises(ValueError):
            Task(description="Task", priority=3, status=-1)

        task.status = 0
        assert task.status == 0
        with pytest.raises(ValueError):
            task.status = 5

    def test_is_ready_for_execution(self) -> None:
        task = Task(description="Task", priority=3, status=0)
        assert task.is_ready_for_execution is True

        task.priority = 5
        assert task.is_ready_for_execution is True

        task.status = 1
        assert task.is_ready_for_execution is False
        task.status = 0

        task.priority = 2
        assert task.is_ready_for_execution is False

    def test_status_info_descriptor(self) -> None:
        task = Task(description="Task", priority=3, status=0)

        with pytest.raises(AttributeError):
            _ = task.status_info

        task.__dict__["status_info"] = "Custom Info"
        assert task.status_info == "Custom Info"
