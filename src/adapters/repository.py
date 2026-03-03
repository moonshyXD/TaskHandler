from src.domain.task import Task


class TaskRepository:
    def __init__(self) -> None:
        """
        Инициализировать хранилище задач
        """
        self._tasks: list[Task] = []

    def save_all(self, tasks: list[Task]) -> None:
        """
        Сохранить список задач в хранилище
        :param tasks: Список задач
        """
        self._tasks.extend(tasks)

    def get_all(self) -> list[Task]:
        """
        Получить все сохраненные задачи из хранилища
        :return: Список всех задач
        """
        return self._tasks
