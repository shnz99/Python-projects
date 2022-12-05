from dataclasses import asdict
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker =CoffeeMaker()
money_machine = MoneyMachine()

run = True
while run:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        run = False
    else:
        choice = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(choice) and money_machine.make_payment(choice.cost): # type: ignore
            coffee_maker.make_coffee(choice)
