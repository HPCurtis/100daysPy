from morse import morse_code
from sys import exit

def main():

    # Repeat if KeyError is caught form index of the dictionary until proper inputs provided    
    while True:
        try:
            # Take the user input strip whitespace and ocnvert all text uppercase for dictinary comparison
            string = input("Please enter text for Morse code conversion: ").strip().upper()
              # Generate empty string for updating
            morse_string = ""
            for c in string:
                # Find the morse code conversion 
                # stored in the morse code dictionary.
                morse_string += morse_code[c] + " "
                
            # while loop break
            break
        except KeyError:
            pass
        except EOFError:
            if EOFError:
                exit()
    
    # print the morse code string conversion
    print(morse_string)

if __name__ == "__main__": 
    main()