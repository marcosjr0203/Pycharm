"""
100 DAYS OF CODE
DAY 9
TODO-1 Create a program that work out as a bid auction, where each user makes a bid.
 At the end, the program has to loop through the dictionary with the names as keys and bids as its values
 in order to find and print the name of the auction's winner and the value that he bidded.
"""
bids = {}


def highest_bid(bid_list):
    highest = 0
    winner = ""
    bank = {}
    for item in bid_list:
        bank = bid_list
        if bid_list[item] > highest:
            winner = item
            highest = bid_list[item]
    print(f"Results:\nThese where the bids: {bank}\nThe winner is {winner} with a bid of ${highest:.2f}")


restart = True
while restart is True:
    name = input("Name: ")
    bid = input("Bid: $")
    while not bid.isnumeric():
        print("Wrong answer. Try again.")
        bid = input("Bid: $")
    bid = float(bid)
    yn = input("Press [y] to insert new data. ")
    while yn not in "yn":
        print("Wrong answer. Try again.")
        yn = input("Press [y] to insert new data. ")
    if yn.lower() != "y":
        restart = False
    bids[name] = bid
highest_bid(bid_list=bids)


