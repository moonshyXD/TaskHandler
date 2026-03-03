from typing import Any

from src.domain.errors import ContractViolationError
from src.domain.repository import TaskRepositoryI
from src.domain.task_source import TaskSource


class ImportTasks:
    def __init__(self, repository: TaskRepositoryI):
        self.repository = repository

    def execute(self, source: Any) -> int:
        if not isinstance(source, TaskSource):
            raise ContractViolationError(source_obj=source)

        new_tasks = source.get_tasks()
        self.repository.save_all(new_tasks)

        return len(new_tasks)
