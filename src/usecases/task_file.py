import json

from src.domain.task import Task


class TaskFile:
    def __init__(self, file_path: str):
        """
        Инициализировать источник задач из файла
        :param file_path: Путь к файлу с задачами
        """
        self.file_path = file_path

    def get_tasks(self) -> list[Task]:
        """
        Прочитать и распарсить задачи из файла
        :return: Список задач, загруженных из файла
        """
        file_path = self.file_path
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        tasks = []
        for line in lines:
            _, payload = line.split(" ", 1)
            task = Task(payload=json.loads(payload))
            tasks.append(task)

        return tasks
