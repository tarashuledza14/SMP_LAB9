from Lib.Log import logger


class Exporter:
    def __init__(self, figure):
        self.figure = figure
        logger.info("Об'єкт Exporter створено для фігури: %s", repr(figure))

    def export_as_png(self, filename):
        try:
            self.figure.savefig(filename + ".png")
            logger.info("Файл успішно збережено у форматі PNG: %s.png", filename)
        except Exception as e:
            logger.error("Помилка при експорті у форматі PNG: %s. Помилка: %s", filename, e)
            raise

    def export_as_svg(self, filename):
        try:
            self.figure.savefig(filename + ".svg")
            logger.info("Файл успішно збережено у форматі SVG: %s.svg", filename)
        except Exception as e:
            logger.error("Помилка при експорті у форматі SVG: %s. Помилка: %s", filename, e)
            raise