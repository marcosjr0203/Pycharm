"""
TODO 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
import math as m
s = float(input("Enter the size of the wall to be painted, in square meters: \n"))
print(f"To paint {s}m² of wall, you'll need {s/3:.2f} liters of paint.\n")
if s/3 >= 1:
    print(f"We only sell 18 liter cans of paint, so you will have to buy {m.ceil(s/3/18)} cans.\n")
    print(f"Each can cost $80.00, so this will cost a total of ${(m.ceil(s / 3 / 18)) * 80:.2f}")
elif s/3 > 0 < 1:
    print(f"We only sell 18 liter cans of paint, so you will have to buy {m.ceil(s / 3 / 18)} can.\n")
    print("Each can cost $80.00")
else:
    print("GET OUT FROM MY STORE!!!!!!!!")