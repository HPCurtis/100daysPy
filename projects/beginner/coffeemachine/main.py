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
    while True:
        order = process_user_order(resources)
        order = resource_check(order)
        coins = coin_insert()
        coins_sum = coins_process(coins)
        transaction_check(order, coins_sum)
        make_coffee(order)

def process_user_order(resources):
    options = ["espresso", "latte", "cappuccino"] 

    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ").strip().lower() 
        
        if order == "off":
            sys.exit()

        elif order == "report":
            for key, value in resources.items():
                if key == "water" or key == "milk":
                    print(key.capitalize(), str(value) + "ml")
                elif value == "coffee":
                    print(key.capitalize(), str(value) + "g")

        elif order in options:
            return order

def coin_insert():
    print("please insert coins.")
    n_quarters = get_pos_int("How many quarters?: ")
    n_dimes = get_pos_int("How many dimes?: ")
    n_nickels = get_pos_int("How many nickles?: ")
    n_pennies = get_pos_int("How many pennies?: ")

    coins = {
        "quarters": n_quarters,
        "dimes": n_dimes,
        "nickels": n_nickels,
        "pennies": n_pennies
    }
    
    return coins

def resource_check(order): 
    resource_req = MENU[order]['ingredients']
    list_tf = []

    for key, value in resource_req.items():
        if value <= resources.get(key, 0):
            list_tf.append(True)
        else:
            print(f"Sorry, there is not enough {key}")
            list_tf.append(False)

    if not all(list_tf):
       order = process_user_order(resources)
       return order
    else:
        return order
    
    
def coins_process(coins):
    coins_sum = 0
    coin_values = {
        "quarters": .25,
        "dimes": .1,
        "nickels": .05,
        "pennies": .01
    }
    for coin, value in coin_values.items():
        coins_sum += coins[coin] * value
    
    return coins_sum

def transaction_check(order, coins_sum):
    resource_req = MENU[order]['cost']
    
    if coins_sum == resource_req:
         if 'money' in resources:
            resources['money'] += resource_req
         else:
            resources['money'] = resource_req

    elif coins_sum < resource_req:
        print("Sorry that's not enough money. Money refunded.")

    elif coins_sum > resource_req:
        # Add profit to the resource dictionary
        if 'money' in resources:
            resources['money'] += resource_req
        else:
            resources['money'] = resource_req            
        change = round(coins_sum - resource_req, 2)
        print(f"Here is {change} dollars in change")
        
def make_coffee(order):
    c_resources = MENU[order]["ingredients"]
    for key in c_resources:
        resources[key] -= c_resources[key]
    print(f"Here is your {order}. Enjoy!")

def get_pos_int(prompt):
    while True:
        user_input = input(prompt)
        try:
            integer_value = int(user_input)
            if integer_value < 0:
                raise ValueError
            return integer_value
        except ValueError:
            pass

def check_all_true(lst):
    return all(lst)
if __name__ == "__main__":
    main()