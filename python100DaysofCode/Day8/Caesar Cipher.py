"""
100 DAYS OF CODE
DAY 8
CHALLENGE: CAESAR CIPHER
TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in
    the alphabet by the shift amount and print the encrypted text.
    HINT: How do you get the index of an item in a list:
    https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
TODO-3: Call the encrypt function and pass in the user inputs. You should be able to
test the code and encrypt a message.
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'a', 'b',
            'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']

def encrypt(text, shift):
    for letter in range(text):
        print(shift + letter)
text = input("Insert message: ")
shift = input("Insert shift: ")
encrypt(text, shift)

