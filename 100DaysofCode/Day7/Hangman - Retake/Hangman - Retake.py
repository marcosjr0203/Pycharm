"""
Make a Hangman game.
"""
import random
import ascii
from words_bank import words
message = " Welcome to the Hangman "
print(f"\033[31m{message.upper():¤^50}\033[0;0m")
opt = ["animals", "archeology", "countries", "food", "miscellaneous",
       "mithology", "movies", "objects", "sports", "technology"]
for item, x in enumerate(opt):
    print(f"{item+1}-{x.upper()}")
choice = int(input("Pick a theme, or type 0 for random: "))
if choice == 0:
    secret_list = list(words[random.choice(opt)])
else:
    secret_list = list(words[opt[choice-1]])
secret_word = random.choice(secret_list)
display = []
chances = 5
for letter in secret_word:
    display += "_"
while True:
    if display == list(secret_word):
        print(ascii.win)
        break
    print(f"\33[33m\nYou have {chances} chance\33[0;0m", end="")
    print("\33[33ms\33[0;0m") if chances > 1 else print("\n")
    guess = input("\33[33mType your guess: \33[0;0m")
    if guess in secret_word:
        for item, char in enumerate(secret_word):
            if char == guess:
                display[item] = char
        print(display)
    else:
        print(display)
        chances -= 1
        print(ascii.stages[chances])
        if chances == 0:
            print(f"\33[41mYOU LOOSE\33[0;0m\nThe word is \33[34m{secret_word.upper()}")
