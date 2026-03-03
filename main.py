from src.adapters.cli import CLI
from src.adapters.repository import TaskRepository
from src.domain.errors import ContractViolationError, InputValidationError
from src.usecases.import_tasks import ImportTasks
from src.usecases.task_api import TaskAPI
from src.usecases.task_file import TaskFile
from src.usecases.task_random import TaskRandom


def run() -> None:
    """
    Запуск интерактивного обработчика задач
    """
    CLI.greet()
    repo = TaskRepository()
    importer = ImportTasks(repository=repo)

    while (action := CLI.action_select()) != CLI.EXIT:
        try:
            match action:
                case CLI.TASKS_FROM_FILE:
                    file_path = CLI.get_file_path()
                    tasks_file_obj = TaskFile(file_path=file_path)
                    importer.execute(tasks_file_obj)

                case CLI.TASKS_RANDOM:
                    tasks_count = CLI.get_tasks_count()
                    tasks_random_obj = TaskRandom(tasks_count=tasks_count)
                    importer.execute(tasks_random_obj)

                case CLI.TASKS_API:
                    tasks_api_obj = TaskAPI()
                    importer.execute(tasks_api_obj)

                case CLI.CHECK_TASKS:
                    saved_tasks = repo.get_all()
                    CLI.print_tasks(tasks=saved_tasks)

        except InputValidationError as e:
            print(f"Ошибка ввода: \n{e}")
        except ContractViolationError as e:
            print(f"Ошибка системы \n{e}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: \n{e}")

    CLI.goodbye()


if __name__ == "__main__":
    run()
