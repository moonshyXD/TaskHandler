from typing import Any


class TaskHandlerError(Exception):
    pass


class InputValidationError(TaskHandlerError):
    def __init__(self, field: str, value: Any, reason: str):
        self.field = field
        self.value = value
        self.reason = reason
        message = (
            f"Некорректное значение в поле '{self.field}': {self.reason}"
            f"Передано: {self.value}"
        )

        super().__init__(message)


class ContractViolationError(TaskHandlerError):
    def __init__(self, source_obj: Any):
        self.source_type = type(source_obj).__name__
        message = (
            f"Объект типа '{self.source_type}' "
            "не поддерживает требуемый поведенческий контракт"
        )

        super().__init__(message)
