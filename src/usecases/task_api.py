from src.domain.task import Task


class TaskAPI:
    def get_tasks(self) -> list[Task]:
        """
        Получить список задач из API-заглушки
        :return: Список сгенерированных задач
        """
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
        task1 = Task(payload=payload1)
        task2 = Task(payload=payload2)
        tasks = [task1, task2]
        return tasks
