from src.domain.task import Task


class TaskRepository:
    def __init__(self) -> None:
        """
        Инициализировать хранилище задач
        """
        self._tasks: list[Task] = []
        self._next_id: int = 1

    def save_all(self, tasks: list[Task]) -> None:
        """
        Сохранить список задач в хранилище
        :param tasks: Список задач
        """
        for task in tasks:
            task.id = self._next_id
            self._next_id += 1
            self._tasks.append(task)

    def get_all(self) -> list[Task]:
        """
        Получить все сохраненные задачи из хранилища
        :return: Список всех задач
        """
        return self._tasks
