import sys
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def main():
    order = get_user_order()

def get_user_order():
    options = ["espresso", "latte", "cappuccino"] 

    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ").strip().lower() 

        if order == "off":
            sys.exit()
        elif order in options:
            return order

if __name__ == "__main__":
    main()