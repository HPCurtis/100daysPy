import os

def clear_screen():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def user_input():
    num1 = first_num()
    print("+\n-\n*\n/")
    op = pick_an_operator()
    num2 = next_num()
    return num1, op, num2

def continue_f(result):    
    cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    return cont

def operator_eval(num1, operator, num2):
    if(operator == '+'):
        result = num1 + num2
        result_s = (f"{num1} + {num2} = {result}")
        return result, result_s
    elif(operator == '-'):
        result = num1 - num2
        result_s = (f"{num1} - {num2} = {result}")
        return result, result_s
    elif(operator == '*'):
        result = num1 * num2
        result_s = (f"{num1} * {num2} = {result}")
        return result, result_s
    elif(operator == '/'):
        result = num1 / num2
        result_s = (f"{num1} * {num2} = {result}")
        return result,  result_s
    else:
        print('Sorry, but I cannot understand your operation')

def pick_an_operator():
    valid_operators = {'+', '-', '*', '/'}

    while True:
        user_input = input("Pick and operator: ").strip()
        if user_input in valid_operators:
            return user_input
        else:
            print("Invalid operator. Please enter a valid operator.")

def first_num():

    while True:
        try:
            user_input = float(input("What's the first number?: ").strip())
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.") 

def next_num():
    while True:
        try:
            user_input = float(input("what's the next number?:").strip())
            return user_input
        except ValueError:
                print("Invalid input. Please enter a valid number.") 