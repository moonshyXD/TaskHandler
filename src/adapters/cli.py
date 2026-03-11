import questionary

from src.domain.descriptors import FilePathValidator, TaskCountValidator
from src.domain.task import Task


class GenerateTasksRequest:
    count = TaskCountValidator()


class GenerateFilePathRequest:
    file_path = FilePathValidator()


class CLI:
    GREET_MESSAGE = "Приветствуем вас в интекративном обработчике задач!"
    GOODBYE_MESSAGE = "Спасибо, что работали с нами. До свидания!"

    TASKS_FROM_FILE = "Задачи из файла"
    TASKS_RANDOM = "Рандомные задачи"
    TASKS_API = "Задачи из API-заглушки"
    CHECK_TASKS = "Просмотреть список задач"
    EXIT = "Выход из программы"

    ACTION_ASK = "Выберите режим приёмки задач"
    TASKS_COUNT_ASK = "Какое количество заданий вы хотите сгенерировать?"
    FILE_PATH_ASK = "Укажите путь к файлу (относительно папки TaskHandler)?"

    @staticmethod
    def get_tasks_count() -> int:
        """
        Запросить у пользователя количество задач для генерации
        :return: Количество задач
        """
        raw_input = questionary.text(CLI.TASKS_COUNT_ASK).ask()
        request = GenerateTasksRequest()
        request.count = raw_input
        return request.count

    @staticmethod
    def get_file_path() -> str:
        """
        Запросить у пользователя путь к файлу с задачами
        :return: Путь к файлу
        """
        raw_input = questionary.text(CLI.FILE_PATH_ASK).ask()
        request = GenerateFilePathRequest()
        request.file_path = raw_input
        return request.file_path

    @staticmethod
    def greet() -> None:
        """
        Вывести приветственное сообщение
        """
        print(CLI.GREET_MESSAGE)

    @staticmethod
    def action_select() -> str:
        """
        Запросить у пользователя выбор действия из меню
        :return: Выбранное пользователем действие
        """
        action = questionary.select(
            CLI.ACTION_ASK,
            choices=[
                CLI.TASKS_FROM_FILE,
                CLI.TASKS_RANDOM,
                CLI.TASKS_API,
                CLI.CHECK_TASKS,
                CLI.EXIT,
            ],
        ).ask()

        return action

    @staticmethod
    def goodbye() -> None:
        """
        Вывести прощальное сообщение
        """
        print(CLI.GOODBYE_MESSAGE)

    @staticmethod
    def print_tasks(tasks: list[Task]) -> None:
        """
        Вывести список задач в консоль
        :param tasks: Список задач
        """
        for task in tasks:
            print(task.id, task.description, task.priority, task.status)
