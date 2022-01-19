"""
100 DAYS OF CODE
DAY 9
"""
# HINT: You can call clear() to clear the output in the console.
from turtle import clear
print("Welcome to the Blind Auction!")


def validation(yn):
    while yn != "Y".lower() and yn != "N".lower():
        print("Error: type only 'y' or 'n'")
        yn = input("Wanna bid? [ Y | N ] : ").lower()


bids = {}
winner = ""
max_bid = 0
ans = input("Wanna bid? [ Y | N ] : ").lower()
validation(ans)
while ans != "n":
    name = input("Type your name: ")
    bid = float(input("Type your bid: "))
    if bid > max_bid:
        max_bid = bid
        winner = name
    clear()
    ans = input("Wanna bid? [ Y | N ] : ").lower()
    validation(ans)
print(f"Winner: {winner}, with a bid of $ {max_bid}")
