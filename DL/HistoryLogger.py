class HistoryLogger:
    history = []

    @staticmethod
    def log(command, result):
        HistoryLogger.history.append({"command": command, "result": result})

    @staticmethod
    def show_history():
        for record in HistoryLogger.history:
            print(f"Команда: {record['command']}")
            print(f"Результат: {record['result']}")
