import random
import string
import unittest
from Lab_2.calculator import Calculator


class CalculatorAdditionUnitTests(unittest.TestCase):
    def test_add_positive_numbers_returns_correct_value(self):
        # Arrange
        calculator = Calculator()
        test_num1 = random.randrange(1, 100) * 1.0
        test_num2 = random.randrange(1, 100) * 1.0
        operator = "+"
        expected = test_num1 + test_num2
        calc = calculator.calculate(test_num1, test_num2, '+')

        # Assert
        self.assertEqual(expected, calc)

    def test_add_negative_numbers_returns_correct_value(self):
        # Arrange
        calculator = Calculator()
        test_num1 = random.randrange(-100, -1) * 1.0
        test_num2 = random.randrange(-100, -1) * 1.0
        operator = "+"
        expected = test_num1 + test_num2
        calc = calculator.calculate(test_num1, test_num2, '+')

        # Assert
        self.assertEqual(expected, calc)

    def test_add_positive_and_negative_numbers_returns_correct_value(self):
        # Arrange
        calculator = Calculator()
        test_num1 = random.randrange(-100, -1) * 1.0
        test_num2 = random.randrange(1, 100) * 1.0
        operator = "+"
        expected = test_num1 + test_num2
        calc = calculator.calculate(test_num1, test_num2, '+')

        # Assert
        self.assertEqual(expected, calc)

    def test_add_positive_numbers_returns_correct_value(self):
        # Arrange
        calculator = Calculator()
        test_num1 = random.randrange(1, 100) * 1.0
        test_num2 = random.randrange(1, 100) * 1.0
        operator = "+"
        expected = test_num1 + test_num2
        calc = calculator.calculate(test_num1, test_num2, '+')

        # Assert
        self.assertEqual(expected, calc)

