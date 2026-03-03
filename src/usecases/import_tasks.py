from typing import Any

from src.domain.errors import ContractViolationError
from src.domain.repository import TaskRepositoryI
from src.domain.task_source import TaskSource


class ImportTasks:
    def __init__(self, repository: TaskRepositoryI):
        """
        Инициализировать импорт задач
        :param repository: Интерфейс хранилища задач
        """
        self.repository = repository

    def execute(self, source: Any) -> int:
        """
        Выполнить импорт задач из указанного источника
        :param source: Объект источника задач
        :raises ContractViolationError: Если источник не поддерживает контракт
        :return: Количество успешно загруженных задач
        """
        if not isinstance(source, TaskSource):
            raise ContractViolationError(source_obj=source)

        new_tasks = source.get_tasks()
        self.repository.save_all(new_tasks)

        return len(new_tasks)
