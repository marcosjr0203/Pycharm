"""
100 DAYS OF CODE
DAY 8
1- Create a function called "greet()";
2- Write 3 "print" statements inside the function;
3- Call the greet() function and run your code.
"""
# # Simple function
#
#
# def greet():
#     print("Good morning")
#     print("Have a nice day")
#     print("Good bye!")
#
#
# greet()

# # A function that allows for input
#
#
# def greet(name):  # greet = parameter; name = argument
#     print(f"Good morning, {name}")
#     print(f"Have a nice day, {name}")
#     print(f"Good bye, {name}!")
#
#
# greet("Marcos")

# # A function with two inputs
#
#
# def greet(name, location):  # greet = parameter; name, location = argument; name&location = positional argument.
#     print(f"Good morning, {name}")
#     print(f"How is the weather in {location}?")
#     print(f"Good bye, {name}!")
#
#
# greet("Marcos", "Várzea Paulista")
# greet("Samira", "Ribas do Rio Pardo")

# A function with keywords


def greet(name, location):  # greet = parameter; name, location = argument; name&location = positional argument.
    print(f"Good morning, {name}")
    print(f"How is the weather in {location}?")
    print(f"Good bye, {name}!")


greet(location="Várzea Paulista", name="Marcos")

