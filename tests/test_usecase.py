from unittest.mock import mock_open, patch

import pytest

from src.domain.errors import ContractViolationError
from src.domain.task import Task
from src.usecases.import_tasks import ImportTasks
from src.usecases.task_api import TaskAPI
from src.usecases.task_file import TaskFile
from src.usecases.task_random import TaskRandom


class MockRepo:
    def __init__(self) -> None:
        self.saved: list[Task] = []

    def save_all(self, tasks: list[Task]) -> None:
        self.saved = tasks

    def get_all(self) -> list[Task]:
        return self.saved


class TestUseCases:
    def test_task_api(self) -> None:
        assert len(TaskAPI().get_tasks()) == 2

    def test_task_random(self) -> None:
        tasks = TaskRandom(3).get_tasks(1)
        assert len(tasks) == 3
        assert tasks[0].payload["priority"] in TaskRandom.PRIORITIIES
        assert tasks[0].payload["description"] in TaskRandom.DESCRIPTIONS
        assert tasks[0].payload["status"] in TaskRandom.STATUSES
        assert tasks[0].id is None

    @patch("builtins.open", mock_open(read_data='1 {"a": 1}'))
    def test_task_file(self) -> None:
        tasks = TaskFile("goose.txt").get_tasks()
        assert tasks[0].id is None and tasks[0].payload == {"a": 1}

    def test_import_tasks_success(self) -> None:
        repo = MockRepo()
        count = ImportTasks(repo).execute(TaskAPI())
        assert count == 2 and len(repo.saved) == 2

    def test_import_tasks_fail(self) -> None:
        with pytest.raises(ContractViolationError):
            ImportTasks(MockRepo()).execute(123)
