from typing import Any
from unittest.mock import patch

from src.adapters.cli import CLI
from src.domain.task import Task


class TestCLI:
    @patch("src.adapters.cli.questionary.text")
    def test_get_tasks_count(self, mock_text: Any) -> None:
        mock_text.return_value.ask.return_value = "5"
        assert CLI.get_tasks_count() == 5

    @patch("src.adapters.cli.questionary.text")
    def test_get_file_path(self, mock_text: Any, tmp_path: Any) -> None:
        f = tmp_path / "test.txt"
        f.touch()
        mock_text.return_value.ask.return_value = str(f)

        assert str(CLI.get_file_path()) == str(f)

    @patch("builtins.print")
    def test_greet_and_goodbye(self, mock_print: Any) -> None:
        CLI.greet()
        CLI.goodbye()
        assert mock_print.call_count == 2

    @patch("src.adapters.cli.questionary.select")
    def test_action_select(self, mock_select: Any) -> None:
        mock_select.return_value.ask.return_value = CLI.EXIT
        assert CLI.action_select() == CLI.EXIT

    @patch("builtins.print")
    def test_print_tasks(self, mock_print: Any) -> None:
        CLI.print_tasks([Task(id=1, payload={"a": 1})])
        assert mock_print.call_count == 2
