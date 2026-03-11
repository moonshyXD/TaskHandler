import datetime

from src.domain.descriptors import (
    DescriptionValidator,
    PriorityValidator,
    StatusInfoDescriptor,
)


class Task:
    priority = PriorityValidator()
    description = DescriptionValidator()

    # Non-data descriptor для демонстрации отличий.
    status_info = StatusInfoDescriptor()

    def __init__(
        self,
        description: str,
        priority: int,
        status: int,
        id: int | None = None,
    ) -> None:
        """
        Инициализировать задачу
        :param description: Описание задачи
        :param priority: Приоритет задачи
        :param status: Статус задачи
        :param id: Идентификатор задачи
        """
        self._id = id
        self.description = description
        self.priority = priority
        self.status = status
        self._created_at = datetime.datetime.now()

    @property
    def id(self) -> int | None:
        """
        Получить идентификатор задачи
        :return: Идентификатор задачи
        """
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def status(self) -> int:
        """
        Получить статус задачи
        :return: Статус задачи
        """
        return self._status

    @status.setter
    def status(self, value: int) -> None:
        """
        Установить статус задачи
        :param value: Новое значение статуса
        :raise ValueError: Если статус не 0 и не 1
        """
        if value not in (0, 1):
            raise ValueError(
                "Статус должен быть 0 (не выполнено) или 1 (выполнено)"
            )
        self._status = value

    @property
    def created_at(self) -> datetime.datetime:
        """
        Получить время создания задачи
        :return: Время создания
        """
        return self._created_at

    @property
    def task_duration(self) -> datetime.timedelta:
        """
        Получить длительность существования задачи
        :return: Длительность существования
        """
        return datetime.datetime.now() - self.created_at

    @property
    def is_ready_for_execution(self) -> bool:
        """
        Проверить готовность задачи к выполнению
        :return: Истина, если задача готова
        """
        return self.status == 0 and self.priority >= 3

    @property
    def short_description(self) -> str:
        """
        Получить краткое описание задачи
        :return: Первые 10 символов описания
        """
        desc = self.description
        return f"{desc[:10]}..." if len(desc) > 10 else desc
