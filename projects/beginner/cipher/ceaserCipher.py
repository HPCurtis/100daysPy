# Fix wrap around bug and the avoiding of punctuation or blank spaces.

from cipherart import ca

# Define alphabet variable
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# prijt ASCI art.git 
print(ca())

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(direction, text, shift):
    # Create empty list of shifted index values.
    index_s = []
    encrypted_word = []
    
    for i in text:
        index = alphabet.index(i)

        if direction == 'encode':    
            encrypted_word.append(alphabet[index + shift])
        elif direction == 'decode':
            encrypted_word.append(alphabet[index - shift])

    encrypted_word = ''.join(encrypted_word)
    print(f"The {direction} text is {encrypted_word}")

ceaser(direction, text, shift)