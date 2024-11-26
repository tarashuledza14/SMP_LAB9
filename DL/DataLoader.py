import pandas as pd

from Lib.Log import logger


class DataLoader:
    def __init__(self, filepath):
        logger.info("Створення об'єкта DataLoader для файлу: %s", filepath)
        try:
            self.data = pd.read_csv(filepath)
            logger.info("Дані успішно завантажені з файлу: %s", filepath)
        except FileNotFoundError:
            logger.error("Файл не знайдено: %s", filepath)
            raise
        except pd.errors.EmptyDataError:
            logger.error("Файл пустий або містить некоректні дані: %s", filepath)
            raise
        except Exception as e:
            logger.error("Невідома помилка при завантаженні файлу: %s. Помилка: %s", filepath, e)
            raise

    def get_data(self):
        logger.info("Отримання даних з DataLoader")
        return self.data
