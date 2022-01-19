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
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def cypher():
    option = int(input("Choose an option below: \n""1 - Encrypt\n""2 - Decrypt\n""Opt.: "))
    message = input("Insert the message (no spaces, no special characters): ")
    shift = int(input("Inform shift value: "))
    m_ind = []
    ciphered = ""
    for letter in message.lower():
        m_ind.append(letters.index(letter))
    if option == 1:
        for ind in m_ind:
            ciphered += letters[ind+shift]
    elif option == 2:
        for ind in m_ind:
            ciphered += letters[ind-shift]
    print(ciphered)


cypher()
