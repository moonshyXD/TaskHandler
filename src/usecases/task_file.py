import json

from src.domain.task import Task


class TaskFile:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_tasks(self) -> list[Task]:
        file_path = self.file_path
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        tasks = []
        for line in lines:
            id, payload = line.split(" ", 1)
            task = Task(id=int(id), payload=json.loads(payload))
            tasks.append(task)

        return tasks
