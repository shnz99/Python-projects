from data import MENU, resources
from os import system, name

resources['money'] = 0

# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def user_input():
    """Ask user to input desired Coffee. Hidden values are 'off' and 'report'."""
    user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    clear()
    return user_prompt

def turn_off_machine():
    """Turn off the Coffee Machine by entering 'off' to the prompt."""
    print("Coffe Machine is shutting down...")
    return False

def report(data):
    """Print the resources left in the machine by entering 'report' to prompt."""
    water = f"Water: {data['water']}ml"
    milk = f"Milk: {data['milk']}ml"
    coffee = f"Coffee: {data['coffee']}g"
    money = f"Money: ${data['money']}"
    print(f"{water}\n{milk}\n{coffee}\n{money}")

def check_suff_res(coffee, data):
    """Checking if there are sufficient resources for desired coffee and returning True or False."""
    ingredients = MENU[coffee]['ingredients']
    for i in ingredients:
        if ingredients[i] >= data[i]:
            return i
    return True

def process_coins():
    """Ask user to insert coins and return sum."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def decrease(resource, coffee):
    """Get used resources and coffee ingredients and return reduced resources."""
    decreased_res = resource
    for i in coffee:
        decreased_res[i] -= coffee[i]
    return decreased_res

def coffee_machine():
    """Program to make you a coffee."""
    used_resources = resources
    machine_running = True
    
    while machine_running:
        
        coffee = user_input()
        if coffee == 'off':
            return turn_off_machine()
        elif coffee == 'report':
            report(used_resources)
            continue
        elif coffee == 'espresso' or coffee == 'latte' or coffee == 'cappuccino':
            check_ingredient = check_suff_res(coffee, used_resources)
            
            if check_ingredient == True:
                user_money = process_coins()
                coffee_cost = MENU[coffee]['cost']
                coffee_ingredients = MENU[coffee]['ingredients']
                
                if user_money >= coffee_cost:
                    change = round(user_money - coffee_cost, 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {coffee} ☕ enjoy.")
                    
                    used_resources = decrease(used_resources, coffee_ingredients)
                    used_resources['money'] += coffee_cost
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Sorry there is not enough {check_ingredient}.")
        else:
            continue
        
coffee_machine()