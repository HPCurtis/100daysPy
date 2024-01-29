def main():
   bt, np, tp = user_input()
   tcs = tip_calc_split(bt, np, tp)
   bs = bill_split(bt, np)
   person_pays = bs + tcs
   print(f"Each person should pay: ${round(person_pays,1)}")

def user_input():
    # Generate greeting for the tip calcaulator
    print("Welcome to the tip calculator.")

    bill_total = input("What was the total of the bill? $")
    number_of_people = input("How many people to split the bill? ")
    tip_per = input("What percentage tip would you like to give ? 10, 12, or 15? ")
    return bill_total, number_of_people, tip_per

def tip_calc_split(total, n_people, percent):
    return  ( (float(total) * 0.01) * int(percent) ) / int(n_people)  

def bill_split(total, n_people):
    return float(total) / int(n_people)

if __name__ == "__main__":
    main()