from Lib import functions
from configs import global_value


class Calculator:
    def __init__(self):
        """Initialize the Calculator with memory value from global settings."""
        self.memory_value = global_value.memory_value

    def get_input(self):
        """
        Get user input for operands and operator.
        This function handles input validation for operands and operators.
        """
        while True:
            try:
                # Get the first operand, or recall it from memory
                user_input = input('Input first operand (or MR for memory recall): ').upper()
                if user_input == 'MR':
                    first_operand = self.memory_value
                    print(f"Recalled from memory: {first_operand}")
                else:
                    first_operand = float(user_input)

                # Get and validate the operator
                operator = input("Input operator (+, -, *, /, ^, %, sq): ").strip()
                if not self.validate_operator(operator):
                    print("Invalid operator. Try again.")
                    continue

                # Get the second operand, or recall it from memory
                while True:
                    user_input = input('Input second operand (or MR for memory recall): ').upper()
                    if user_input == 'MR':
                        second_operand = self.memory_value
                        print(f"Recalled from memory: {second_operand}")
                    else:
                        second_operand = float(user_input)

                    # If division operator, check for zero in the second operand
                    if operator == '/' and second_operand == 0:
                        print("Error: Division by zero is not allowed. Please enter a non-zero second operand.")
                    else:
                        break  # Exit the loop if the second operand is valid

                return first_operand, second_operand, operator

            except ValueError:
                print("Invalid number format. Try again.")

    def validate_operator(self, operator):
        """
        Validate if the operator is in the list of supported operators.
        """
        valid_operators = ['+', '-', '*', '/', '^', '%', 'sq']
        return operator in valid_operators

    def calculate(self, first_operand, second_operand, operator):
        """
        Perform the calculation based on the operator and operands.
        This function handles errors like division by zero and invalid square roots.
        """
        try:
            result = functions.choose_operator(first_operand, second_operand, operator)
            # Log the history of the calculation
            functions.log_history(first_operand, operator, second_operand, round(result, global_value.round_number))
            return round(result, global_value.round_number)

        except (ZeroDivisionError, ValueError) as e:
            print(e)
            return None

    def run(self):
        """
        Main loop for running the calculator.
        This handles memory operations and allows the user to perform calculations repeatedly.
        """
        while True:
            first_operand, second_operand, operator = self.get_input()
            result = self.calculate(first_operand, second_operand, operator)
            if result is not None:
                print(f"Result: {result}")

            choice_memory = input(
                'Would you like to store result in memory (MS), add to memory (M+), clear memory (MC), or skip? '
            ).upper()

            match choice_memory:
                case 'MS':
                    self.memory_value = result
                    print(f"Stored {result} in memory.")
                case 'M+':
                    self.memory_value += result
                    print(f"Added {result} to memory. New memory value: {self.memory_value}.")
                case 'MC':
                    self.memory_value = 0
                    print("Memory cleared.")

            if input("Do you want to view history? (yes/no): ").strip().lower() == 'yes':
                print(functions.show_history())

            if input('Do you want to make another calculation? (yes/no): ').lower() != 'yes':
                break