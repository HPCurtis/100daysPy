from clear import clear_terminal
from auctionart import logo

print(logo())
print("Welcome to the secret auction program.")

# Generate emyt list to get the dictionry of names and lists.
names_bids = []

# Use a while to keep getting resposive if there are more bidders 
while True:
    # Get user input. 
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    others = input("Are there any other bidders? Type 'yes' or 'no',\n").strip().lower()

    new_dict = {'name': name, 'bid': bid}
    names_bids.append(new_dict)

    # Use conditonal statement to deal with potenial of more bidders
    if others == "yes":
        # Use clear_terminal fucntion so other bidders cannot see the last bid.
        clear_terminal()
    elif others == "no":
        # No more bidders so break from the while loop.
        break

# Generate empty name and bid lists
names = []
bids = []
# loop through names and bids and append to the respective lists.
for i in names_bids:
    names.append(i["name"])
    bids.append(i["bid"])

# Get max bid and its index.
max_bid, max_bid_index = max(bids), bids.index(max(bids))
# Get the winner names using the index.
Winners_name = names[max_bid_index]

# Output the winner
print(f"The winner is {Winners_name} with a bid of {max_bid}" )