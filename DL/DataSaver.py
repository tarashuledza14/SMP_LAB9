from Lib.Log import logger
import json
import csv


class DataSaver:
    @staticmethod
    def save_as_json(data, filename):
        try:
            with open(f"{filename}.json", "w") as f:
                json.dump(data, f)
            logger.info("Дані успішно збережені у форматі JSON: %s.json", filename)
        except Exception as e:
            logger.error("Помилка при збереженні даних у форматі JSON: %s. Помилка: %s", filename, e)
            raise

    @staticmethod
    def save_as_csv(data, filename):
        try:
            with open(f"{filename}.csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data[0].keys())  # Запис заголовків
                for row in data:
                    writer.writerow(row.values())
            logger.info("Дані успішно збережені у форматі CSV: %s.csv", filename)
        except Exception as e:
            logger.error("Помилка при збереженні даних у форматі CSV: %s. Помилка: %s", filename, e)
            raise

    @staticmethod
    def save_as_txt(data, filename):
        try:
            with open(f"{filename}.txt", "w") as f:
                for item in data:
                    f.write(str(item) + "\n")
            logger.info("Дані успішно збережені у форматі TXT: %s.txt", filename)
        except Exception as e:
            logger.error("Помилка при збереженні даних у форматі TXT: %s. Помилка: %s", filename, e)
            raise
