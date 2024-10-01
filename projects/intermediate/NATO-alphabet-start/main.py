import pandas as pd 

df = pd.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:

phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(phonetic_dict)

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Select a word: ").upper()

# Generate output list.
output_list = [phonetic_dict[letter] for letter in word]

# print to console the phoenticv output of that word.
print(output_list)