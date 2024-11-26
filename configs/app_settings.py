from . import global_value

def setting():
    while True:
        print("1. The value after the comma")
        print("0. Back to main menu")

        menu_setting = input('Enter your choice: ')

        match menu_setting:
            case '1':
                global_value.round_number=int(input('Enter number after comma: '))
            case '0':
                break