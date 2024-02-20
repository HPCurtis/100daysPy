#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

def number_1_100():
    return random.randint(1, 100)

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.") 

def greeting():
    print("Weclome to the number guessing game!\n" +
        "I'm thinking of a number between 1 and 100.")

def get_difficulty():
    while True:
        try:
            user_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
            print(user_input)
            if user_input != "easy" and user_input != "hard":
                raise ValueError
            return user_input
        except ValueError:
                print("You did not type easy or hard correctly, please try again")

def difficulty_check(diff):
    if diff == "hard":
        return 5
    elif diff == "easy":
        return 10

def guessing_game(number):
    global guesses_left
    guess = get_int("Make a Guess: ")

    if guess == number:
        return "That is correct"
    elif guess > number:
        guesses_left -= 1
        return "Guess is to large"
    elif guess < number:
        guesses_left -= 1
        return "Guess is too small"

# Generate random number between 0 and 100.
number = number_1_100()
# Greet the user.
greeting()
# Get the difficulty of the game the user will play
difficulty = get_difficulty()
guesses_left = difficulty_check(difficulty)

while guesses_left > 0:
    print(f"you have {guesses_left} attempts left to guess the number")
    result = guessing_game(number)
    print(result)
    if result == "That is correct":
        print(f"You got it the answer was {number}")
        break

if guesses_left == 0:
    print("You ran out of guesses")



   

