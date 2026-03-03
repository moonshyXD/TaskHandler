from src.domain.task import Task


class TaskAPI:
    def get_tasks(self) -> list[Task]:
        payload1 = {
            "description": "Эта первая задача для гуся",
            "priority": "Высокий",
            "status": "Активна",
        }
        payload2 = {
            "description": "Эта вторая задача для гуся",
            "priority": "Низкий",
            "status": "Неактивна",
        }
        task1 = Task(id=52, payload=payload1)
        task2 = Task(id=53, payload=payload2)
        tasks = [task1, task2]
        return tasks
