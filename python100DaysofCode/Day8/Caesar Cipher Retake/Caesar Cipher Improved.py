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
TODO-8: Validate all the inputs
"""
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def cypher(opt, msg, shf):
    msg_indx = []
    ciphered = ""
    if opt == 1:
        for item in msg:
            if item in letters:
                msg_indx.append(letters[letters.index(item)+shf])
            else:
                msg_indx.append(item)
    elif opt == 2:
        for item in msg:
            if item in letters:
                msg_indx.append(letters[letters.index(item)-shf])
            else:
                msg_indx.append(item)
    for item in msg_indx:
        ciphered += str(item)
    print(ciphered)


def menu():
    option = input("Choose an option below: \n""1 - Encrypt\n""2 - Decrypt\n""Opt.: ")
    if option in "12":
        option = int(option)
    else:
        while option != 1 and not option == 2:
            print("Wrong option, try again.")
            menu()
    message = input("Insert the message (no spaces, no special characters): ").lower()
    shift = input("Inform shift value: ")
    while not shift.isnumeric():
        print("Try again.")
        shift = input("Inform shift value: ")
    shift = int(shift)
    if shift > len(letters):
        while shift > len(letters):
            shift = shift // len(letters)
    cypher(opt=option, msg=message, shf=shift)
    restart = input("Do you want to restart the program [y/n]? ").lower()
    if restart == "y":
        menu()
    else:
        pass


menu()



