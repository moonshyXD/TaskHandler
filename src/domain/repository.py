from typing import Protocol

from src.domain.task import Task


class TaskRepositoryI(Protocol):
    def __init__(self) -> None:
        """
        Инициализировать хранилище задач
        """
        ...

    def save_all(self, tasks: list[Task]) -> None:
        """
        Сохранить список задач в хранилище
        :param tasks: Список задач
        """
        ...

    def get_all(self) -> list[Task]:
        """
        Получить все сохраненные задачи из хранилища
        :return: Список всех задач
        """
        ...
