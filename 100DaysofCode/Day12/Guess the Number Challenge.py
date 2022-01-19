import logo
from random import randint
print(logo.start_logo)
number = randint(0, 100)
level = input("Choose a level - [H]ard or [Easy]: ").lower()
if level == "h":
    chances = 5
elif level == "e":
    chances = 10
print("I'm thinking on a number from 0 to 100. Try to guess it.")
guess = int(input("Type a number: "))

while guess != number:
    if chances != 0:
        if guess < number:
            chances -= 1
            print(f"You have {chances} chances left")
            guess = int(input(f"{guess} is lower than the chosen number. Try again: "))

        elif guess > number:
            chances -= 1
            print(f"You have {chances} chances left")
            guess = int(input(f"{guess} is higher than the chosen number. Try again: "))
    else:
        print(logo.lose_logo)
else:
    print(logo.win_logo)