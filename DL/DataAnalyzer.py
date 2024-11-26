from Lib.Log import logger

class DataAnalyzer:
    def __init__(self, data):
        self.data = data
        logger.info("DataAnalyzer створено з даними розміром %s", data.shape)

    def get_extreme_values(self):
        logger.info("Викликається функція get_extreme_values")
        try:
            extreme_values = self.data.describe().loc[['min', 'max']]
            logger.info("Успішно отримано екстремальні значення")
            return extreme_values
        except Exception as e:
            logger.error("Помилка у get_extreme_values: %s", e)
            raise