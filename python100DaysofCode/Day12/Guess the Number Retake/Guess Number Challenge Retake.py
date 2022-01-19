"""
100 DAYS OF CODING
DAY 12
"""
import random
import Arts
import time


def start():
    print(Arts.title)
    guess_number()


def difficulty():
    chance = 0
    diff = input("\33[32m[E]\33[0;0masy or "
                 "\33[32m[H]\33[0;0mard\n"
                 "Choose a level: ")
    while diff.upper() not in "EH":
        diff = input("Wrong Option.\n"
                     "\33[32m[E]\33[0;0masy or "
                     "\33[32m[H]\33[0;0mard\n"
                     "Choose a level: ")
    if diff.upper() == "E":
        chance = 10
    elif diff.upper() == "H":
        chance = 5
    return chance


def restart():
    r = input("Restart [y/n]? ")
    while r.lower() not in "yn":
        r = input("Wrong answer.\nRestart [y/n]? ")
    if r.lower() == "y":
        start()
    elif r.lower() == "n":
        print(Arts.thank)
        time.sleep(0.5)
        print(Arts.you)
        time.sleep(0.5)
        print(Arts.ffor)
        time.sleep(0.5)
        print(Arts.playing)


def is_numeric(g):
    while not g.isnumeric():
        g = input("Wrong answer. Type a number between 1 and 100: ")
    return int(g)


def guess_number():
    chances = difficulty()
    print("I'm thinking in a number between 1 and 100.\n"
          f"You have {chances} attempts left.")
    number = random.randint(0, 100)
    guess = is_numeric(input("Make a guess: "))
    while chances > 1:
        if guess > 100:
            guess = is_numeric(input("Type a number between 1 and 100: \n"
                                     "Make another guess: "))
        if guess > number:
            chances -= 1
            guess = is_numeric(input("Too high.\n"
                                     f"You have {chances} attempts left.\n"
                                     "Make another guess: "))
        elif guess < number:
            chances -= 1
            guess = is_numeric(input("Too low.\n"
                                     f"You have {chances} attempts left.\n"
                                     "Make another guess: "))
        elif guess == number:
            print(Arts.win)
            restart()
            break
    if chances == 1:
        print(Arts.loose)
        restart()


start()





