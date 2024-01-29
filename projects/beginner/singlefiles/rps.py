rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

def main():
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n").strip())
    rps(user_choice)
    # Generate computers choice of rock, paper, scissors.
    computer_c_choice = random_rps_choice()
    rps(computer_c_choice)

    # Output result 
    win_determination(user_choice, computer_c_choice)

def rps(i):
    if i == 0:
        print(rock)
    elif i == 1:
        print(paper)
    elif i == 2:
        print(scissors)

def random_rps_choice():
    nums = [0,1,2]
    return random.choice(nums)

def win_determination(user_c, computer_c):
    if user_c == computer_c:
        return print("It's a tie!")
    elif (
        (user_c == 0 and computer_c == 2) or
        (user_chouser_cice == 2 and computer_c == 1) or
        (user_c == 1 and computer_c == 0)
    ):
        print("You win")
    else:
        return print("You lose")

if __name__ == "__main__":
    main()