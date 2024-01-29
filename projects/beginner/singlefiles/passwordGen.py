#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def main():
    nr_l, nr_s, nr_n = user_input()
    letter_rs, symbols_rs, numbers_rs = random_sample(nr_l, nr_s, nr_n, 
                                                      letters, numbers, symbols)
    # Combine the lists
    combined_res = letter_rs + symbols_rs + numbers_rs
    random.shuffle(combined_res)
    combined_res = ''.join(combined_res)

    print(combined_res)

def user_input():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    return nr_letters, nr_symbols, nr_numbers

def random_sample(nr_l, nr_s, nr_n, letters, symbols, numbers):
    # Generate randomly sampled letters, symblos and numbers based on user input
    letters_rs = random.sample(letters, nr_l)
    symbols_rs = random.sample(symbols, nr_s)
    numbers_rs = random.sample(numbers, nr_n)
    return letters_rs, symbols_rs, numbers_rs


if __name__ == "__main__":
    main()

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P