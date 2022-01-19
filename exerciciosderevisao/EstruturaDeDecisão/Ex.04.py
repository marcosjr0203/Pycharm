"""
TODO 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letter = input("Enter a letter: ")
if letter.isnumeric():
    print(f"'{letter.upper()}' is a number.")
elif letter.isalpha():
    if letter == "a" \
            or letter == "e" \
            or letter == "i" \
            or letter == "o" \
            or letter == "u":
        print(f"'{letter.upper()}' is vogal.")
    else:
        print(f"'{letter.upper()}' is consonant.")
else:
    print(f"'{letter.upper()}' is a symbol.")