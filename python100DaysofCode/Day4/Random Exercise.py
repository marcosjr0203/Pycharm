"""
Create a virtual coin toss program. It'll randomly return "Heads" or "Tails", by asking a seed number to the user.
"""
import random
seed = int(input("Enter the seed: "))
toss = random.randint(0, 1)
if toss == 0:
    print("Heads.")
else:
    print("Tails.")
print(toss)
