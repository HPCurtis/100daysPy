
from higherlowerart import logohl, vslogo
from game_data import gdata
import random
import os

def main_call(count):
    print(logohl())
    
    if count > 0:
        clear_screen()
        print(logohl())
        print(f"You're right! Current score is: {count}")
    
    _, fc_a = compare_a()
    print(vslogo())
    _, fc_b = against_b()
    user_input = get_a_or_b()
    result = compare_ab(user_input, fc_a, fc_b)
    return fc_a, fc_b, user_input, result

def clear_screen():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_random_number():
    """
    Generates and returns a random number between 0 and 49.
    """
    return random.randint(0, len(gdata()))
def a_or_b():
    user_input = input("Who has more followers?: Type A or B: ").lower().strip()
    return user_input

def get_a_or_b():
    """
    Prompts the user to enter a mathematical operator (+, -, *, /) and returns the entered operator.
    Keeps prompting until a valid operator is provided.
    """
    valid_operators = {'a', 'b'}

    while True:
        user_input = a_or_b()
        if user_input in valid_operators:
            return user_input
        else:
            print("Please enter a A or B for valid response")

def get_data():
    rn = generate_random_number()
    response = gdata()[rn]
    followerc = response.pop("follower_count")
    return response, followerc

def compare_a():
    resp, fc = get_data()
    print(f"Compare A: {resp['name']}, a {resp['description']}, from  {resp['country']}")
    return resp, fc

def against_b():
    resp, fc = get_data()
    print(f"Against A: {resp['name']}, a {resp['description']}, from  {resp['country']}")
    return resp, fc

def compare_ab(user_i, a, b):
    if a > b and user_i == 'a':
        return True
    elif a < b and user_i == 'b':
        return True
    elif a > b and user_i == 'b':
        return False
    elif a < b and user_i == 'a':
        return False
        
