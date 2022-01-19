import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
           "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "9", "8", "0"]
symbols = ["!", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "_", "+", "=", "-"]
characters = []
password = ""
for item in range(0, 4):
    characters += random.choice(letters)
for item in range(0, 2):
    characters += random.choice(numbers)
    characters += random.choice(symbols)
random.shuffle(characters)
for item in characters:
    password += item
print(password)