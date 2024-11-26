from configs import global_value


def addition(a,b):
    c = a + b
    
    return c

def subtraction(a,b):
    c = a - b
    
    return c

def division(a,b):

    while b == 0:
        print('You cannot divide by zero! Enter another number.')
        b = float(input('Input second operand: '))
    
    c = a / b
    
    return c

def multiplication(a,b):
    c = a * b
    
    return c

def power(a,b):
    c = a ** b
    
    return c

def square_root(a,b):
    c = a ** (1/b)
    
    return c

def modulus(a,b):
    c = a%b  
      
    return c

def log_history(first_operand, operator, second_operand, result):
    with open('history_log.txt', 'a') as file:
        file.write(f"{first_operand} {operator} {second_operand} = {result}\n")

def show_history():
    try:
        with open('history_log.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "No history found."

def choose_operator(first_operand, second_operand, operator):
    try:
        match operator:
            case '+':
                result = addition(first_operand, second_operand)
            case '-':
                result = subtraction(first_operand, second_operand)
            case '/':
                if second_operand == 0:
                    raise ZeroDivisionError("Error: Division by zero is not possible.")
                result = division(first_operand, second_operand)
            case '*':
                result = multiplication(first_operand, second_operand)
            case '^':
                result = power(first_operand, second_operand)
            case 'sq':
                if first_operand < 0:
                    raise ValueError("Error: Negative number under the root.")
                result = square_root(first_operand, second_operand)
            case '%':
                result = modulus(first_operand, second_operand)

        return result
    except (ZeroDivisionError, ValueError) as e:
        print(e)
        return None

def show_menu():
    print("Main Menu")
    print("1. Calculator")
    print("2. Settings")
    print("0. Exit")