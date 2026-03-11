from unittest.mock import mock_open, patch

import pytest

from src.domain.errors import ContractViolationError
from src.domain.task import Task
from src.repository.task_api import TaskAPI
from src.repository.task_file import TaskFile
from src.repository.task_random import TaskRandom
from src.usecases.import_tasks import ImportTasks


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
        random_source = TaskRandom(tasks_count=3)
        tasks = random_source.get_tasks()
        assert len(tasks) == 3
        assert 1 <= tasks[0].priority <= 5
        assert tasks[0].description in TaskRandom.DESCRIPTIONS
        assert tasks[0].status in TaskRandom.STATUSES
        assert tasks[0].id is None

    def test_task_file(self) -> None:
        file_content = (
            '1 {"description": "Test", "priority": 1, "status": 0, "id": 1}\n'
        )
        with patch("builtins.open", mock_open(read_data=file_content)):
            tasks = TaskFile("dummy_path.txt").get_tasks()

            assert len(tasks) == 1
            assert tasks[0].id == 1
            assert tasks[0].description == "Test"
            assert tasks[0].priority == 1
            assert tasks[0].status == 0

    def test_import_tasks_success(self) -> None:
        repo = MockRepo()
        importer = ImportTasks(repo)
        count = importer.execute(TaskAPI())
        assert count == 2
        assert len(repo.saved) == 2

    def test_import_tasks_fail(self) -> None:
        with pytest.raises(ContractViolationError):
            ImportTasks(MockRepo()).execute(123)
