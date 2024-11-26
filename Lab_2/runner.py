from Lib import functions
from Lab_2.calculator import Calculator
from configs import app_settings


def run():
    calculator = Calculator()
    while True:
        functions.show_menu()
        choice = input('Enter your choice: ').strip()

        match choice:
            case '1':
                calculator.run()
            case '2':
                app_settings.setting()
            case '0':
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")
