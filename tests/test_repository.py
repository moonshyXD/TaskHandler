from pathlib import Path

import pytest

from src.domain.task import Task
from src.repository.task_api import TaskAPI
from src.repository.task_file import TaskFile
from src.repository.task_random import TaskRandom


class TestRepositories:
    def test_task_api(self) -> None:
        api_source = TaskAPI()
        tasks = api_source.get_tasks()

        assert isinstance(tasks, list)
        assert len(tasks) == 2
        assert all(isinstance(t, Task) for t in tasks)
        assert tasks[0].description == "Эта первая задача для гуся"
        assert tasks[0].status == 1

    def test_task_random(self) -> None:
        count = 5
        random_source = TaskRandom(tasks_count=count)
        tasks = random_source.get_tasks()

        assert len(tasks) == count
        assert all(isinstance(t, Task) for t in tasks)

        for task in tasks:
            assert 1 <= task.priority <= 5
            assert task.status in (0, 1)
            assert len(task.description) > 0

    def test_task_file(self) -> None:
        project_root = Path(__file__).parent.parent.resolve()
        file_path = project_root / "test.txt"

        if not file_path.exists():
            pytest.skip(f"Test file not found at {file_path}")

        file_source = TaskFile(file_path=str(file_path))
        tasks = file_source.get_tasks()

        assert len(tasks) == 3
        assert tasks[0].id == 1
        assert tasks[0].description == "Сделать лабу идеально"
        assert tasks[0].priority == 5
        assert tasks[0].status == 0

        assert tasks[1].id == 2
        assert tasks[1].status == 1
