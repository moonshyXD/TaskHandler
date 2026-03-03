from typing import Protocol

from src.domain.task import Task


class TaskRepositoryI(Protocol):
    def save_all(self, tasks: list[Task]) -> None: ...
    def get_all(self) -> list[Task]: ...
