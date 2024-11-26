from typing import List, Dict


class HistoryLogger:
    """A class for logging commands and their results."""

    def __init__(self):
        self.history: List[Dict[str, str]] = []

    def log(self, command: str, result: str) -> None:
        """Logs a command and its result into the history."""
        self.history.append({"command": command, "result": result})

    def show_history(self) -> None:
        """Displays the history of logged commands and results."""
        for record in self.history:
            print(f"Команда: {record['command']}")
            print(f"Результат: {record['result']}")
