letters = ["a", "b", "c", "d", "e",
           "f", "g", "h", "i", "j",
           "k", "l", "m", "n", "o",
           "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z"]
message = "Hello World"
# m_ind = []
# for item in message.lower():
#     m_ind.append(letters.index(item))
# print(m_ind)

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
TODO-4: Make the code into a function with 3 inputs: option, message, shift.
TODO-5: Improve your code for keeping numbers, symbols and spaces among the ciphered text
TODO-6: Ask the user if he want to restart the program, after using it.
TODO-7: Create a way of make the shift work out even if the user input a greater number than the letters list.
"""
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def cypher(opt, msg, shf):
    m_ind = []
    ciphered = ""
    for letter in msg.lower():
        if letter.isalpha():
            m_ind.append(letters.index(letter))
        else:
            m_ind.append(letter)
    if opt == 1:
        for ind in m_ind:
            if m_ind[ind].isalpha():
                ciphered += letters[ind+shf]
            else:
                ciphered += m_ind[ind]
    elif opt == 2:
        for ind in m_ind:
            if m_ind[ind].isalpha():
                ciphered += letters[ind-shf]
            else:
                ciphered += m_ind[ind]
    print(ciphered)


option = int(input("Choose an option below: \n""1 - Encrypt\n""2 - Decrypt\n""Opt.: "))
message = input("Insert the message (no spaces, no special characters): ")
shift = int(input("Inform shift value: "))
cypher(opt=option, msg=message, shf=shift)

