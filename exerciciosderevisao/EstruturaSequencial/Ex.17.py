"""
TODO 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
18.1. comprar apenas latas de 18 litros;
18.2. comprar apenas galões de 3,6 litros;
18.3. misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
arredonde os valores para cima, isto é, considere latas cheias.
"""
import math as m
s = float(input("Inform the size of the wall to be painted, in m²: "))
p = s / 6
t = p
bc = 0
sc = 0
while t > 0:
    if t/18 > 1:
        bc += 1
        t -= 18
    elif t/18 > 0 < 1:
        sc += 1
        t -= 3.6
print(f"-OPTION 1: BUYING ONLY 18 LITERS CANS\n"
      f"\tAmount of Cans:\n"
      f"\t{m.ceil(p/18)} can of 18 liter, $80.00 each, total of ${m.ceil(p/18)*80:.2f}\n"
      f"-OPTION 2: BUYING ONLY 3.6 LITERS CANS\n"
      f"\tAmount of Cans:\n"
      f"\t{m.ceil(p/3.6)} can of 3.6 liter, $25.00 each, total of ${m.ceil(p/3.6)*25:.2f}\n"
      f"-OPTION 3: BOTH SIZES\n"
      f"\tAmount of cans: {bc} of 18 liter and {sc} of 3.6 liter.\n"
      f"\tTotal: \n"
      f"\t1- {bc} can of 18 liter, $80.00 each, total of ${bc*80:.2f}\n"
      f"\t2- {sc} can of 3.6 liter, $25.00 each, total of ${sc*25:.2f}\n"
      f"Total cost: ${bc*80+sc*25:.2f}")
