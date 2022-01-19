"""
Create a program that asks two informations and joint than as a band name.
E.g.:
Input1 = name of the city where do you live: Boston;
Input2 = name of your favorite food: Pizza; Output = "Boston Pizza"
"""
welcome = " Welcome to the band name generator! "
print(f"{welcome:§^60}")
city = input("What's the name of the city you grew up in? ")
pet = input("What's your pet name's? ")
print(f"Your band name should be {city} {pet}")
