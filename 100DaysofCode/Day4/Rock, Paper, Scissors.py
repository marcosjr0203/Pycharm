"""
Make a program that work out as a "Rock, Paper & Scissors" game.
"""
import RPSArt
import random
from time import sleep


def rps():
    wlcm = " Rock, Paper & Scissors "
    print(f"{wlcm:▒^50}")
    while True:
        opt = input("Choose your option: \n"
                    "[1] rock\n"
                    "[2] paper\n"
                    "[3] scissor\n"
                    "[0] to stop game\n"
                    "Choose: ")
        if not opt.isnumeric():
            print("Wrong option. Try again.")
            rps()
        else:
            opt = int(opt)
            if opt == 0:
                print(RPSArt.bye)
                break
            else:
                opt = opt-1
            if 0 < opt > 2:
                print("Wrong option. Try again.")
                rps()
            else:
                print(f"YOUR CHOICE:\n", RPSArt.user[opt])
        cpu = random.randint(0, 2)
        print(f"CPU'S CHOICE:\n", RPSArt.comp[cpu])
        sleep(0.5)
        print(".", end="")
        sleep(0.5)
        print(".", end="")
        sleep(0.5)
        print(".", end="")
        sleep(0.5)
        if abs(opt-cpu) < 2:
            if opt < cpu:
                print(RPSArt.loose)
            elif opt > cpu:
                print(RPSArt.win)
            else:
                print(RPSArt.draw)
        else:
            if opt == 0:
                print(RPSArt.win)
            else:
                print(RPSArt.loose)


rps()
