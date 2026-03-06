from src.adapters.repository import TaskRepository
from src.domain.task import Task


class TestRepository:
    def test_repository_operations(self) -> None:
        repo = TaskRepository()
        assert repo.get_all() == []

        repo.save_all([Task(id=1, payload={"a": 1})])
        tasks = repo.get_all()

        assert len(tasks) == 1
        assert tasks[0].id == 1
