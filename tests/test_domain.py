from src.domain.errors import ContractViolationError, InputValidationError
from src.domain.task import Task
from src.domain.task_source import TaskSource


class TestDomain:
    def test_task_creation(self) -> None:
        t = Task(id=1, payload={"key": "value"})
        assert t.id == 1 and t.payload == {"key": "value"}

    def test_input_error(self) -> None:
        err = InputValidationError("count", "-5", "Reason")
        assert "count" in str(err) and "-5" in str(err)

    def test_contract_error(self) -> None:
        err = ContractViolationError(123)
        assert "int" in str(err) and "не поддерживает" in str(err)

    def test_protocol_typing(self) -> None:
        class ValidSource:
            def get_tasks(self) -> list[Task]:
                return []

        valid_obj = ValidSource()
        assert isinstance(valid_obj, TaskSource)
        assert valid_obj.get_tasks() == []
        assert not isinstance(123, TaskSource)
