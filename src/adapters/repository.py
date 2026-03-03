from src.domain.task import Task


class TaskRepository:
    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def save_all(self, tasks: list[Task]) -> None:
        self._tasks.extend(tasks)

    def get_all(self) -> list[Task]:
        return self._tasks
