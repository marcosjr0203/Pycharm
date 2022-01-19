"""
TODO 17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou
 não bissexto.
"""
year = int(input("Type the year: "))
if year % 400 == 0:
    print(f"{year} is a leap year.")
    if year % 100 == 0:
        print(f"{year} is not a leap year.")
        if year % 4 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is a leap year.")




