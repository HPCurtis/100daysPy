#Challlenge 1 
import random
import hangmanwords
import hangmanart

print(hangmanart.hmASCI())

word_list = hangmanwords.wl()
lives = 6

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
display = []
for i in range(len(chosen_word)):
    display.append('_')


# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please guess a letter ").lower()

while True:
    # Loop through and update the guess to the display list
    for i, letter in enumerate(chosen_word):
        if guess == letter:
            display[i] = letter
            print(f"{' '.join(display)}")
            print(hangmanart.hmstages()[lives])
    
    if guess not in chosen_word:
        
        lives -= 1
        print(f"{' '.join(display)}")
        print(hangmanart.hmstages()[lives])

    if '_' in display:
            guess = input("Please guess a letter ").lower()
    else:
      print("You've won")
      break
    
    if lives == 0:
      print("You've lost")
      break

   
