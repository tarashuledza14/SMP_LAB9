import logging
import pandas as pd

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("data_analyzer.log"),
        #logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)