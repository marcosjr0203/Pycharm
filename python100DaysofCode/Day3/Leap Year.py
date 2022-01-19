"""
Write a program that works out whether if a given year is a leap year.
A leap year is defined when it's divisible by 4 and not divisibe by 100, unless it's also divisible by 400.
"""
year = int(input("Insert year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
