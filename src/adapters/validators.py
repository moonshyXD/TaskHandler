from pathlib import Path
from typing import Any  # <--- Добавляем импорт Any

from src.domain.errors import InputValidationError


class TaskCountValidator:
    REASON_INT = "Должно вводиться целое число"
    REASON_NOT_NEGATIVE = "Число должно быть неотрицательным"

    def __set_name__(self, owner: Any, name: str) -> None:
        self.name = name

    def __set__(self, instance: Any, value: Any) -> None:
        try:
            val_int = int(value)
        except ValueError:
            raise InputValidationError(
                field=self.name, reason=self.REASON_INT, value=value
            ) from None

        if val_int < 0:
            raise InputValidationError(
                field=self.name, reason=self.REASON_NOT_NEGATIVE, value=value
            )

        instance.__dict__[self.name] = val_int


class FilePathValidator:
    REASON_NOT_STRING = "Путь должен быть строкой"
    REASON_NOT_EXISTS = "Файл по указанному пути не найден"
    REASON_NOT_FILE = "Указанный путь ведет к папке, а надо к файлу"

    def __set_name__(self, owner: Any, name: str) -> None:
        self.name = name

    def __set__(self, instance: Any, value: Any) -> None:
        if not isinstance(value, str):
            raise InputValidationError(
                field=self.name, reason=self.REASON_NOT_STRING, value=value
            )

        path = Path(value).resolve()
        if not path.exists():
            raise InputValidationError(
                field=self.name, reason=self.REASON_NOT_EXISTS, value=str(path)
            )

        if not path.is_file():
            raise InputValidationError(
                field=self.name, reason=self.REASON_NOT_FILE, value=str(path)
            )

        instance.__dict__[self.name] = path
