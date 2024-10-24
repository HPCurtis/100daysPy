# Import necessary packages.
from random import sample
import os
from deck import cards_dict, card_list
from art import blasci

def main():
    
    # Create a while loop to get user input until the end of the game or exit is made by the user.
    while True:
        # Get user choice to play or not
        choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

        if choice == 'y':
            # Clear the terminal screen before proceeding.
            os.system('clear')  # or use os.system('cls') for Windows
            print(blasci)
            blackjack(cl=card_list, cd=cards_dict)
            break
        elif choice == 'n':
            break
        else:
            print("Please select an appropriate input")

def blackjack(cl, cd):
    players_score = []
    computers_score = []

    # Generate player's hand and update the decks.
    players_cards = sample(cl, 2)

    for card in players_cards:
        players_score.append(cd[card])
        cl.remove(card)
    
    print(f"Your cards: {players_score}, current score {sum(players_score)}")

    # Generate the computer's hand.
    computers_cards = sample(cl, 2)
    for card in computers_cards:
        computers_score.append(cd[card])
        cl.remove(card)
        
    print(f"Computer's first card: {computers_cards[0]}")

    # Player game choices
    while True:
        stick_twist = input("Type 'y' to get another card, type 'n' to pass: ")
        if stick_twist == 'y':
            players_card = sample(cl, 1)[0]  # Take the first card from the sample
            cl.remove(players_card)
            players_score.append(cd[players_card])
            print(f"Your cards: {players_score}, current score {sum(players_score)}")
            print(f"Computer's first card: {computers_cards[0]}")
            
        elif stick_twist == 'n':
            break
        else:
            print("Please use an appropriate response as specified")
    
    # Computer's game choices.
    while True:
        if dealer_hit_algo(computers_score, players_score):
            computers_card = sample(cl, 1)[0]  # Take the first card from the sample
            cl.remove(computers_card)
            computers_score.append(cd[computers_card])
            print(f"Your cards: {players_score}, player's final score {sum(players_score)}")
            print(f"Computer's cards: {computers_score} and score {sum(computers_score)}")
        else:
            print(f"Your cards: {players_score}, player's final score {sum(players_score)}")
            print(f"Computer's cards: {computers_score} and score {sum(computers_score)}")
            winner(computers_score, players_score)
            break

def dealer_hit_algo(computer_score, player_score):
    player_total = sum(player_score)
    computer_total = sum(computer_score)
    
    # The computer's decision algorithm on whether to hit
    if player_total > 21:  # Player bust
        return False
    elif computer_total > player_total:  # Computer already won
        return False 
    elif computer_total < player_total and computer_total < 21:  # Computer will try to beat the player
        return True

# Function to check the score of Blackjack and determine the winner
def winner(computer_score, player_score):
    player_total = sum(player_score)
    computer_total = sum(computer_score)

    if player_total > 21:
        print("You lose")
    elif computer_total > 21:
        print("you win")
    elif player_total > computer_total:
        print("You win")
    elif computer_total > player_total:
        print("you lose")
    else: 
        print("You draw")

if __name__ == "__main__":
    main()