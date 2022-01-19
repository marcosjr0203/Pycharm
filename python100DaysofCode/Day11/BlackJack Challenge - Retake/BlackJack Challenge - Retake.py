"""
100 DAYS OF CODE
DAY 11
TODO Write a code for BlackJack game, with the parameters below:
 - Ace worths 1 or 11, which is most convenient to the user;
 - Asks the level to the user, from 1 to 5, representing the number of decks in game (1- hard, 5 easy);
 - The cards has to be removed from the deck as they are drawn;
 - Create a dictionary with the symbols for key and numbers for its value.
"""
import random
import time

deck = {
    "A♣": 1, "2♣": 2, "3♣": 3, "4♣": 4, "5♣": 5, "6♣": 6, "7♣": 7, "8♣": 8, "9♣": 9, "10♣": 10, "Q♣": 10,
    "J♣": 10, "K♣": 10, "A♥": 1, "2♥": 2, "3♥": 3, "4♥": 4, "5♥": 5, "6♥": 6, "7♥": 7, "8♥": 8, "9♥": 9,
    "10♥": 10, "Q♥": 10, "J♥": 10, "K♥": 10, "A♤": 1, "2♤": 2, "3♤": 3, "4♤": 4, "5♤": 5, "6♤": 6, "7♤": 7,
    "8♤": 8, "9♤": 9, "10♤": 10, "Q♤": 10, "J♤": 10, "K♤": 10, "A♢": 1, "2♢": 2, "3♢": 3, "4♢": 4, "5♢": 5,
    "6♢": 6, "7♢": 7, "8♢": 8, "9♢": 9, "10♢": 10, "Q♢": 10, "J♢": 10, "K♢": 10
}
keys_random = []
for item in deck:
    keys_random.append(item)


def hand():
    suit = random.choice(keys_random)
    card_random = deck[suit]
    return suit, card_random


def comp_hand():
    print("Computer's turn: ")
    score = 0
    c = 1
    while score < 15:
        cards = hand()
        score += cards[1]
        print(f"\33[34m{'':->20}\33[0;0m\n"
              f"\33[34m#{c} HAND\33[0;0m\n"
              f"\33[34m{'':->20}\33[0;0m\n"
              f"\33[33mCard: {cards[0]}\n"
              f"\33[33mScore:{score}\33[0;0m")
        if score < 21:
            if "A" in cards[0]:
                if score <= 10:
                    score += 10
                else:
                    score += 1
        elif score == 21:
            print("\33[35mBlack Jack. You loose.\33[0;0m")
            restart()
        elif score > 21:
            print("\33[32mYou win.\33[0;0m")
            restart()
        time.sleep(1)
        c += 1
    return score


def restart():
    cont = input("Start again [y/n]? ")
    while cont not in "yn":
        cont = input("Wrong answer. Start again[y/n]? ")
    if cont == "y":
        winner()


def user_hand():
    print("Your turn: ")
    score = 0
    c = 1
    cont = "y"
    while cont == "y":
        cards = hand()
        score += cards[1]
        print(f"\33[34m{'':->20}\33[0;0m\n"
              f"\33[34m#{c} HAND\33[0;0m\n"
              f"\33[34m{'':->20}\33[0;0m\n"
              f"\33[33mCard: {cards[0]}\n"
              f"\33[33mScore:{score}\33[0;0m")
        if score < 21:
            if cards[1] == 1:
                if score <= 10:
                    score += 11
                else:
                    score += 1
        elif score == 21:
            print(f"\33[32mBlack Jack. You win.\33[0;0m")
            restart()
        elif score > 21:
            print("\33[35mYou loose.\33[0;0m")
            restart()
        cont = input("Do you want one more card [y/n]? ")
        while cont not in "yn":
            cont = input("Wrong answer. Do you want another[y/n]? ")
        if cont == "n":
            break
        c += 1
    return score


def winner():
    user = user_hand()
    comp = comp_hand()
    if user < 21:
        if user > comp:
            print("\33[32mYou win.\33[0;0m")
            restart()
        elif comp > user:
            print("\33[35mYou loose.\33[0;0m")
            restart()
        else:
            print("\33[33mDraw.\33[0;0m")
            restart()

winner()


