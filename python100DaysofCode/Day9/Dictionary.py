"""
100 DAYS OF CODE
DAY 9
"""
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected. ",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    123: "123"
}
alist = ["One", "Two", "Three", "Etcera"]
# retrieve an item from a list:
item = alist[0]

# retrieve another item from a dictionary:
another_item = programming_dictionary["Loop"]  # Dont forget the key must be exactly like in the dictionary
another_another_item = programming_dictionary[123]

# adding an item from a dictionary:
programming_dictionary["Error"] = "When something dont work."
print(programming_dictionary)

# create an empty dictionary
empty_dictionary = {}

# editing an item in a dictionary
programming_dictionary[123] = "Just a fucking number"
print(programming_dictionary)

# Looping through a dictionary
for item in programming_dictionary:
    print(item)  # will print only the keys, not its contents
    print(programming_dictionary[item])  # will print the content of each key

# wiping an existing dictionary
programming_dictionary = {}
print(programming_dictionary)


