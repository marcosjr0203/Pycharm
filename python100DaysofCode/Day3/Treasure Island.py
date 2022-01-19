def treasure():
    message = " WELCOME TO THE TREASURE ISLAND "
    print(f"{message:▲^50}")
    print(f"Your Mission is to find the treasure.")
    opt1 = input("Choose your way: Left (l) or Right (r)? ")
    if opt1.lower() == "r":
        print("You fell into a swamp. Game over.")
    elif opt1.lower() == "l":
        opt2 = input("You're in a river bed. What do you wanna do? "
                     "Wait (w) for rescue or swim (s) across? ")
        if opt2.lower() == "s":
            print("You sank in the river. Game over.")
        elif opt2.lower() == "w":
            opt3 = input("You arrived in a castle that has 3 doors:\n "
                         "one red, one yellow, one blue.\n"
                         "You must choose only one.\n"
                         "Which one do you choose? (r), (y), (b): ")
            if opt3.lower() == "r" or opt3.lower() == "b":
                print("You die. Stupid.")
            elif opt3.lower() == "y":
                print("Congrats. You're now the King fucking Arthur.\n"
                      "Here is your fucking crown: |º▲º▲º▲ª|")
            else:
                print("You fucked it up. Start again, motherfucker.")
                treasure()
        else:
            print("You fucked it up. Start again, motherfucker.")
            treasure()
    else:
        print("You fucked it up. Start again, motherfucker.")
        treasure()
treasure()




