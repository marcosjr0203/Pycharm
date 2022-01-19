"""
TODO 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
13.1. Para homens: (72.7*h) - 58
13.2. Para mulheres: (62.1*h) - 44.7
"""


def mci(s):
    if s == "m":
        h = float(input("Type your height: "))
        print(f"Your ideal weight is {(72.7 * h) - 58:.2f}")
    elif s == "f":
        h = float(input("Type your height: "))
        print(f"Your ideal weight is {(62.1 * h) - 44.7:.2f}")


g = input("Type your gender - [m] or [f]: ").lower()
mci(g)
