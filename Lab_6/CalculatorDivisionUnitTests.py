import random
import string
import unittest

from Lab_2.calculator import Calculator


class CalculatorDivisionUnitTests(unittest.TestCase):
    def test_division_of_two_positive_numbers(self):
        # Arrange
        calculator = Calculator()
        number1 = 10
        number2 = 2
        expected_result = 5

        # Act
        actual_result = calculator.division(number1, number2)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_division_of_two_negative_numbers(self):
        # Arrange
        calculator = Calculator()
        number1 = -10
        number2 = -2
        expected_result = 5

        # Act
        actual_result = calculator.division(number1, number2)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_division_of_positive_and_negative_numbers(self):
        # Arrange
        calculator = Calculator()
        number1 = 10
        number2 = -2
        expected_result = -5

        # Act
        actual_result = calculator.division(number1, number2)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_division_of_two_random_numbers(self):
        # Arrange
        calculator = Calculator()
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        expected_result = number1 / number2

        # Act
        actual_result = calculator.division(number1, number2)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_division_of_two_random_float_numbers(self):
        # Arrange
        calculator = Calculator()
        number1 = random.uniform(1, 100)
        number2 = random.uniform(1, 100)
        expected_result = number1 / number2

        # Act
        actual_result = calculator.division(number1, number2)

        # Assert
        self.assertEqual(expected_result, actual_result)