"""
100 DAYS OF CODE
DAY 8
CHALLENGE: HANGMAN
"""
import random
word_list = ["aardvark", "baleia", "camelo", "doninha", "elefante",
             "flamingo", "galinha", "hiena", "iguana", "jararaca",
             "kiwi", "lince", "morsa", "narval", "ovelha", "papagaio",
             "quati", "rinoceronte", "suricate", "tartaruga", "urso",
             "vagalume", "wallaby", "ximango", "yak", "zebra"]

# Step 1
#     TODO-1 - Randomly choose a word from the word_list and assign it to a variable
#     called chosen_word.
chosen_word = random.choice(word_list)
#     TODO-2 - Ask the user to guess a letter and assign their answer to a variable
#     called guess. Make guess lowercase.
"""
# Realocated after step 3
guess = input("Guess a letter: ").lower()

"""
#     TODO-3 - Check if the letter the user guessed (guess) is one of the letters
#     in the chosen_word.
"""
# Just for test
for letter in chosen_word:
    if letter == guess:
        print("Guess")
    else:
        print("Fail")

"""
# Step 2
#     TODO-4: - Create an empty List called display.
#     For each letter in the chosen_word, add a "_" to 'display'.
#     So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"]
#     with 5 "_" representing each letter to guess.
display = []
for letter in range(len(chosen_word)):
    display += "_"

#     TODO-5: - Loop through each position in the chosen_word;
#     If the letter at that position matches 'guess' then reveal that letter in the
#     display at that position.
#     e.g. If the user guessed "p" and the chosen word was "apple", then display
#     should be ["_", "p", "p", "_", "_"].
"""
# Made just for test, and reinserted in the "Todo-7"
for letter in range(0, len(chosen_word)):
    if chosen_word[letter] == guess:
        display[letter] = guess  # Using 'letter' as an index
"""

#     TODO-6: - Print 'display' and you should see the guessed letter in the correct
#     position and every other letter replace with "_".
#     Hint - Don't worry about getting the user to guess the next letter. We'll tackle
#     that in step 7.

# print(display)


# Step 3
#     TODO-7: - Use a while loop to let the user guess again. The loop should only stop
#     once the user has guessed all the letters in the chosen_word and 'display' has no
#     more blanks ("_"). Then you can tell the user they've won.
#     TODO-8: - Create a variable called 'lives' to keep track of the number of lives left.
#     Set 'lives' to equal 6.
#     Check guessed letter
#     TODO-9: - If guess is not a letter in the chosen_word,
#     Then reduce 'lives' by 1.
#     If lives goes down to 0 then the game should stop and it should print "You lose."
#     Join all the elements in the list and turn it into a String.
#     Check if user has got all letters.
game_over = False
from Stages import stages
lives = 6
# Step 4

#     TODO-10: - print the ASCII art from 'stages' that corresponds to the current number
#     of 'lives' the user has remaining.
while game_over is not True:
    # Displaying lives and asking user for a guess
    i = -7 + lives
    print(stages[i])
    print(f"Lives: {lives}")
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
        lives -= 1
    # Replacing '_' for correct guessers
    for letter in range(0, len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess  # Using 'letter' as an index
    print(display)

    # Defining the 'Game Over'
    if lives == 0:
        game_over = True
        print(stages[0])
        print(f"You Lose! The word is {chosen_word}.")
    if not "_" in display:
        game_over = True
        print("You win!")
    if game_over:
        break





