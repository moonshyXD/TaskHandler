from src.adapters.cli import CLI
from src.adapters.logger import logging
from src.adapters.repository import TaskRepository
from src.domain.errors import ContractViolationError, InputValidationError
from src.usecases.import_tasks import ImportTasks
from src.usecases.task_api import TaskAPI
from src.usecases.task_file import TaskFile
from src.usecases.task_random import TaskRandom


def run() -> None:
    """Запуск интерактивного обработчика задач"""
    logging.info("Начало работы программы")
    CLI.greet()

    repo = TaskRepository()
    importer = ImportTasks(repository=repo)

    while (action := CLI.action_select()) != CLI.EXIT:
        try:
            logging.info(f"Пользователь выбрал событие: {action}")
            logging.info(f"Начало выполнения события: {action}")

            match action:
                case CLI.TASKS_FROM_FILE:
                    file_path = CLI.get_file_path()
                    logging.info(
                        f"Пользователь ввел путь к файлу: {file_path}"
                    )
                    importer.execute(TaskFile(file_path=file_path))

                case CLI.TASKS_RANDOM:
                    count = CLI.get_tasks_count()
                    logging.info(f"Пользователь ввел кол-во заданий: {count}")
                    importer.execute(TaskRandom(tasks_count=count))

                case CLI.TASKS_API:
                    importer.execute(TaskAPI())

                case CLI.CHECK_TASKS:
                    saved_tasks = repo.get_all()
                    CLI.print_tasks(tasks=saved_tasks)

            logging.info(f"Успешно выполнено событие: {action}")

        except InputValidationError as e:
            logging.error(f"Ошибка ввода: {e}")
            print(f"Ошибка ввода: \n{e}")

        except ContractViolationError as e:
            logging.error(f"Ошибка системы: {e}")
            print(f"Ошибка системы: \n{e}")

        except Exception as e:
            logging.error(
                f"Произошла непредвиденная ошибка: {e}", exc_info=True
            )
            print(f"Произошла непредвиденная ошибка: \n{e}")

    logging.info("Окончание работы программы")
    CLI.goodbye()


if __name__ == "__main__":
    run()
