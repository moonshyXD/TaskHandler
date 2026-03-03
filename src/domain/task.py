from dataclasses import dataclass


@dataclass
class Task:
    """
    Структура данных, представляющая задачу
    :param id: Идентификатор задачи
    :param payload: Данные задачи
    """

    id: int
    payload: dict
