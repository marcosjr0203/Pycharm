# Todo 1. Prompt user by asking "What would you like [espresso/latte/cappuccino]: "
#  a. Check the user's input to decide what to do next.
#  b. The prompt should show every time action has completed, e.g. once the drink is dispensed.
#  The prompt should show again to serve the next customer.
import ingredients
import logo


def menu():
    print(logo.welcome)
    on = True
    while on is True:
        for n, item in enumerate(ingredients.MENU):
            print(f"[{n+1}] {item}")
        option = input("Choose option: ")
    # Todo 1.
    #  a. For maintainers of the coffee machine, they can use "off" as the secret word to turn it off.
    #  Your code should end execution when this happens.
        if not option.isnumeric():
            if option.lower() not in "offreport":
                print("Wrong option.\n")
                menu()
    # Todo 2. Turn off the Coffee Machine by entering "off" to the prompt.
            elif option.lower() == "off":
                print("\33[31mMachine off\33[0;0m")
                on = False
    # Todo 3. Print report.
    #  a. When  the user enters "report" to the options, a report should be generated that shows the
    #  current resource values. e.g.
    #  Water: 100ml
    #  Milk: 50ml
    #  Coffee: 76g
    #  Money: $2.5
            elif option.lower() == "report":
                print(ingredients.resources)
            else:
                print("Wrong option.")
                menu()
        if option.isnumeric():
            option = int(option)
            res_check(opt=option)


def res_check(opt):
    keyword = ""
    for n, item in enumerate(ingredients.MENU):
        if opt-1 == n:
            keyword = item
    ing = ""
    for ingredient in ingredients.MENU[keyword]["ingredients"]:
        ing = ingredient
# Todo 4. Check if resources are sufficient.
#  a. When the user chooses a drink, the program should check if there are enough resources to make it.
#  b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine, it should not continue
#  to make the drink, but print: "Sorry, there's not enough water."
#  c. The same should happen if another resource is depleted, e.g. milk or coffee.
        if ingredients.resources[ing] < ingredients.MENU[keyword]["ingredients"][ing]:
            print(f"Sorry, there's not enough {ing}.")
            menu()
        else:
            process_coins(key=keyword)
# Todo 5. Process coins.
#  a. If there are sufficient resources to make the drink selected, then the program should prompt the user
#  to insert coins.
#  b. Remember that quarters = $0.25, dimes = $0.10, nickels = $0.05, pennies = $0.01
#  c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies =
#  0.25 + 0+1*2 + 0.05 + 0.01*2 = $0.52.


def process_coins(key):
    drink = key
    cost = ingredients.MENU[key]["cost"]
    amount = 0.0
    vals = []
    for n, item in enumerate(ingredients.values):
        print(f"Press [{n + 1}] for insert {item} (${ingredients.values[item]:.2f})")
        vals.append(ingredients.values[item])
    print(f"Press [{len(vals)+1}] for next step.")
    coins = 0
    while not coins == len(vals)+1:
        coins = input("Option: ")
        while not coins.isnumeric() or int(coins) > len(vals)+1:
            coins = input("\33[31mError. Invalid option.\33[0;0m\nOption: ")
        coins = int(coins)
        if not coins == len(vals)+1:
            amount += vals[coins-1]
        for n, item in enumerate(ingredients.values):
            print(f"[{n + 1}] for insert {item} (${ingredients.values[item]:.2f})")
        print(f"[{len(vals) + 1}] for next step.")
        print(f"{'':-^40}\n"
              f"Drink: {drink}\n"
              f"Price: ${cost:.2f}\n"
              f"\33[31;1;48m${amount:.2f} inserted.\33[0;0m\n"
              f"{'':-^40}")
        if int(coins) == len(vals)+1:
            check_transaction(amount, key)
# Todo 6. Check transaction successful.
#  a. Check that the user has inserted enough money to purchase the drink he selected.
#  E.g. Latte cost $ 2.50, but he only inserted $0.52 then after counting the coins the program should say
#  "Sorry, that's not enough money. Money refunded.".
#  b. But if the user has inserted enough money, than the cost of the drink gets added to the machine as the
#  profit and this will bi reflected the next time "report is triggered.
#  E.g.:
#  Water: 100ml
#  Milk: 50ml
#  Coffee: 76g
#  Money: $2.5


def check_transaction(amnt, k):
    if amnt < ingredients.MENU[k]["cost"]:
        print("Not enough money.\n"
              "\33[31mMoney refunded.\33[0;0m")
        menu()
    elif amnt >= ingredients.MENU[k]["cost"]:
        change = ingredients.MENU[k]['cost']-amnt
        print(f"Take your change: ${abs(change):.2f}")
        ingredients.resources["Funds"] = amnt-change
        make_coffee(k)
# Todo 7. Make Coffee.


def make_coffee(k):
    for item in ingredients.MENU[k]["ingredients"]:
        ingredients.resources[item] -= ingredients.MENU[k]["ingredients"][item]
    print(logo.enjoy)
    menu()


menu()
