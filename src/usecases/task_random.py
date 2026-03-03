import random

from src.domain.task import Task


class TaskRandom:
    DESCRIPTIONS = [
        "Сыграть в казино",
        "Задонатить гусю на пиво",
        "Купить пиво",
        "Поиграть с гусем",
        "Закоммитить в мастер",
        "Покормить гуся",
        "Дать кличку гусю",
        "Завести гуся",
        "Сходить в коворкинг",
        "Приготовить пиццу",
    ]
    PRIORITIIES = ["Высокий", "Средний", "Низкий"]
    STATUSES = ["Активна", "Неактивна"]

    def __init__(self, tasks_count: int):
        self.tasks_count = tasks_count

    def get_tasks(self) -> list[Task]:
        tasks_count = self.tasks_count
        tasks = []
        for task_id in range(tasks_count):
            description = random.choice(self.DESCRIPTIONS)
            priority = random.choice(self.PRIORITIIES)
            status = random.choice(self.STATUSES)
            task = Task(
                id=task_id + 1,
                payload={
                    "description": description,
                    "priority": priority,
                    "status": status,
                },
            )
            tasks.append(task)

        return tasks
