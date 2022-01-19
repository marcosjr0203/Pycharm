"""
TODO 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
n = int(input("Type an integer number: "))
if n > 0:
    print(f"{n} is a positive number.")
elif n == 0:
    print("0 is a neutral number. Neither positive nor negative.")
else:
    print(f"{n} is a negative number.")