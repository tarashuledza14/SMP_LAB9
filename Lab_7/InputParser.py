import re
from typing import Optional


class InputParser:
    """A class to handle parsing of input strings for date and phone number formats."""

    @staticmethod
    def parse_date(input_str: str) -> str:
        """
        Parses a date string in the format YYYY-MM-DD.

        Args:
            input_str (str): The input date string.

        Returns:
            str: A message indicating whether the date format is correct or not.
        """
        if re.match(r'^\d{4}-\d{2}-\d{2}$', input_str):
            return "Дата розпізнана!"
        return "Невірний формат дати"

    @staticmethod
    def parse_phone(input_str: str) -> str:
        """
        Parses a phone number string with an optional '+' prefix and between 7 to 12 digits.

        Args:
            input_str (str): The input phone number string.

        Returns:
            str: A message indicating whether the phone number format is correct or not.
        """
        if re.match(r'^\+?\d[\d -]{7,12}\d$', input_str):
            return "Телефонний номер розпізнано!"
        return "Невірний формат телефону"
