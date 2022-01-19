"""
Write a program that works out whether if a given number is an odd or an even number
"""
n = int(input("Enter an integer number: "))
if n % 2 == 0:
    print(f"{n} is an even number.")
else:
    print(f"{n} is an odd number.")