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


def resources_checker(opt):
    print(f"You choose {opt}\nCost: US${MENU[opt]['cost']:.2f}")
    if opt == "espresso":
        if MENU[opt]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there's not enough water.")
        if MENU[opt]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there's not enough coffee.")
    else:
        if MENU[opt]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there's not enough water.")
        if MENU[opt]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry, there's not enough milk.")
        if MENU[opt]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there's not enough coffee.")
    return resources


# TODO: 1. Prompt user by asking "What would you like [espresso/latte/cappuccino]: "
#     a. Check the user's input to decide what to do next.
#     b. The prompt should show every time action has completed, e.g. once the drink is dispensed.
#     The prompt should show again to serve the next customer.
def machine_on():
    option = input("What would you like [1-espresso/2-latte/3-cappuccino]?: ")  # validation
    resources_checker("espresso")
    while option != "1" and option != "2" and option != "3" and option != "off" and option != "report":
        option = input("Wrong option. Choose [1-espresso/2-latte/3-cappuccino]?: ")
    if option == "1":
        option = "espresso"
    if option == "2":
        option = "latte"
    if option == "3":
        option = "cappuccino"

    # TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
    #     a. For maintainers of the coffee machine, they can use "off" as the secret word to turn it off.
    #     You code should end execution when this happens.

    elif option.lower() == "off":
        print("Machine off.")

    # TODO: 3. Print report.
    #     a. When the user enters "report" to the input, a report should be generated that shows the
    #     current resource values. e.g.
    #     Water: 100ml
    #     Milk: 50ml
    #     Coffee: 76g
    #     Money: $2.5
    elif option.lower() == "report":
        print(resources)

    # TODO: 4. Check if resourses are sufficient.
    #     a. When the user chooses a drink, the program should check if there are enough resources to make it.
    #     b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine, it should not continue
    #     to make the drink, but print: "Sorry, there's not enough water."
    #     c. The same should happen if another resource is depleted, e.g. milk or coffee.

    # if option == "espresso":
    #     resources = MENU[option]["ingredients"]["water"] - resources["water"]
    #     resources = MENU[option]["ingredients"]["coffee"] - resources["coffee"]
    # else:
    #     resources = MENU[option]["ingredients"]["water"] - resources["water"]
    #     resources = MENU[option]["ingredients"]["milk"] - resources["milk"]
    #     resources = MENU[option]["ingredients"]["coffee"] - resources["coffee"]

    if option == "espresso":
        print(MENU[option]["ingredients"]["water"] - resources["water"])
        print(MENU[option]["ingredients"]["coffee"] - resources["coffee"])
    else:
        print(MENU[option]["ingredients"]["water"] - resources["water"])
        print(MENU[option]["ingredients"]["milk"] - resources["milk"])
        print(MENU[option]["ingredients"]["coffee"] - resources["coffee"])

    # TODO: 5. Process coins.
    #     a. If there are sufficient resources to make the drink selected, then the program should prompt the user
    #     to insert coins.
    #     b. Remember that quarters = $0.25, dimes = $0.10, nickes = $0.05, pennies = $0.01
    #     c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies =
    #     0.25 + 0+1*2 + 0.05 + 0.01*2 = $0.52.
    more = "y"
    while more.lower() == "y":
        money = 0

        coins = input("Insert coins:\n"
                      "[1] to insert $0.25 coins\n"
                      "[2] to insert $0.10 coins\n"
                      "[3] to insert $0.05 coins\n"
                      "[4] to insert $0.01 coins\n"
                      "Type your option: ")
        if coins == "1":
            coins = 0.25
        elif coins == "2":
            coins = 0.10
        elif coins == "3":
            coins = 0.05
        elif coins == "4":
            coins = 0.01
        times = int(input(f"How many ${coins:.2f} coins do you wish to insert?: "))  # validation
        amount = coins * times
        print(f"Amount: ${amount:.2f}")
        money += amount
        change = amount - MENU[option]['cost']

        # TODO: 6. Check transaction successful.
        #     a. Check that the user has inserted enough money to purchase the drink he selected.
        #     E.g. Latte cost $ 2.50, but he only inserted $0.52 then after counting the coins the
        #     program should say "Sorry, that's not enough money. Money refunded.".
        #     b. But if the user has inserted enough money, than the cost of the drink gets added
        #     to the machine as the profit and this will be reflected the next time "report is triggered.
        #     E.g.:
        #         Water: 100ml
        #         Milk: 50ml
        #         Coffee: 76g
        #         Money: $2.5
        if MENU[option]['cost'] > money:
            print(f"You inserted ${float(money):.2f}.\n"
                  f"You need to insert more {float(MENU[option]['cost'] - money):.2f}")
        elif MENU[option]['cost'] < money:
            money = amount - change
            print(f"You inserted ${float(money):.2f}.\n"
                  f"Your change: {float(change):.2f}")
        else:
            print(f"You inserted ${float(money):.2f}.\n")
        more = input("Wish to insert more coins [y/n]?: ")  # validation
        if more.lower() == "n" and money < MENU[option]['cost']:
            print("Sorry, that's not enough money. Money refunded.")


        # TODO: 7. Make Coffee.

        elif more.lower() == "n" and money >= MENU[option]['cost']:
            print("Here is your coffee: "
                  """

                 ( (
                ) )
              ........
              |      |]
              \      /
               `----'

            """
                  )
            resources["Money"] = money
            print(resources)
    end = input("End service [y/n]? ")  # validation
    if end == "y":
        machine_on()
    elif end == "n":
        machine_off = True


machine_on()

