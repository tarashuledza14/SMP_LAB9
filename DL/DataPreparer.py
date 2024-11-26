from Lib.Log import logger


class DataPreparer:
    def __init__(self, data):
        logger.info("Створення об'єкта DataPreparer")
        self.data = data

    def prepare_data_for_visualization(self):
        logger.info("Підготовка даних для візуалізації. Початковий розмір: %d рядків, %d стовпців", self.data.shape[0], self.data.shape[1])
        try:
            # Видалення рядків із пропущеними даними
            initial_size = self.data.shape
            self.data.dropna(inplace=True)
            final_size = self.data.shape
            logger.info("Рядки з пропущеними даними видалені. Новий розмір: %d рядків, %d стовпців", final_size[0], final_size[1])

            # Додаткові трансформації можуть бути тут
            return self.data
        except Exception as e:
            logger.error("Помилка під час підготовки даних: %s", e)
            raise