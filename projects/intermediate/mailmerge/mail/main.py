#TODO: Create a letter using starting_letter.txt 
letter = open("Input/Letters/starting_letter.txt", "r")
letter = letter.read()

#for each name in invited_names.txt
names = open("Input/Names/invited_names.txt", "r")
names_r = names.read()
name_list = names_r.replace('\n', ' ').split(" ")

#Replace the [name] placeholder with the actual name.
for name in name_list:
    edited_letter = letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}_invite.txt", "w") as letter_file:
        letter_file.write(edited_letter)

#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp