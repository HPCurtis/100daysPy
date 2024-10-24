# Import neccesary packages.
from random import sample
import os
from deck import cards_dict, card_list
from art import blasci

def main():
    
    # Create while to get user inout until end of game or exit made by user.
    while True:

        # Get user chocie to play or not
        choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

        if choice == 'y':
            # Clear the terminal sscreen before proceding.
            os.system('clear')
            print(blasci)
            blackjack(cl=card_list, cd=cards_dict)
            break
        elif choice =='n':
            break

        # If not correct repsonse given by user prompt use again.
        else:
            print("Please select an appropriate input")

def blackjack(cl, cd):
    players_score = []
    computers_score = []

    # Generate players hand and update the decks.
    players_cards = sample(cl, 2)

    for card in players_cards:
        players_score.append(cd[card])
        cl.remove(card)
    
    print(f"Your cards: {players_score}, current score {sum(players_score)}")

    # Generate the computers hand.
    computers_cards = sample(cl, 2)
    for card in computers_cards:
        computers_score.append(cd[card])
        cl.remove(card)
        
    print(f"Computers first card {computers_score[0]}")


    # Player game choices
    while True:
        stick_twist = input("Type 'y' to get another card, type 'n' to pass: ")
        if stick_twist == 'y':
            players_card = sample(cl, 1)
            cl.remove(players_card[0])
            players_score.append(cd[players_card[0]])
            print(f"Your cards: {players_score}, current score {sum(players_score)}")
            print(f"Computers first card {computers_score[0]}")
            
        elif stick_twist == 'n':
            break
        else:
            print("Please use an appropriate response as specfied")
    
    # Computers game choices.
    while True:
        if dealer_hit_algo(computers_score, players_score):
                computers_card = sample(cl, 1)
                cl.remove(computers_card[0])
                computers_score.append(cd[computers_card[0]])
                print(f"Your cards: {players_score}, players final score {sum(players_score)}")
                print(f"Computers cards {computers_score} and score {sum(computers_score)}")
        else:
            print(f"Your cards: {players_score}, players final score {sum(players_score)}")
            print(f"Computers cards {computers_score} and score {sum(computers_score)}")
            winner(computers_score, players_score)
            break

def dealer_hit_algo(computers_score, players_score):
    players_score = sum(players_score)
    computers_score = sum(computers_score)
    
    # The computers deciosn algortihm on whether to hit

    # If player score has go other 21 the computer 
    # delaer has already one so shouldnt act 
    if players_score > 21:
        return False
    # If the computers score is higher theyve won so stop acting
    elif computers_score > players_score:
        return False 
    # Computer will always attempt to beat the player
    # by acting until score is higher or it busts out.
    elif computers_score <= players_score & computers_score < 21:
        return True

# fucntion to the score of bl and determine the winner
def winner(computers_score, players_score):

    players_score = sum(players_score)
    computers_score = sum(computers_score)

    if players_score > 21:
        print("You lose")
    elif players_score > computers_score:
        print("You win")
    else: 
        print("You lose")


if __name__ == "__main__":
    main()