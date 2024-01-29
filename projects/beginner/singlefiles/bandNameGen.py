# Take user input, cursor sould always bben on ne line when
# awaiting user response

print("Hi, welcome to the band name generator")
# Remove white spaces usign string strip() method.
user_home_town = input("Which city did you grow up in?\n").strip()
user_pet = input("What is a name of a pet?\n").strip()

# Combine users home and pet name.
pet_home_c = user_home_town + " " + user_pet
print("Your band name could be " + pet_home_c )