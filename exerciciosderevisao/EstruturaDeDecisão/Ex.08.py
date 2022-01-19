"""
TODO 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
 decisão é sempre pelo mais barato.
"""
v1 = float(input(f"Insira o 1º valor: "))
v2 = float(input(f"Insira o 2º valor: "))
v3 = float(input(f"Insira o 3º valor: "))
if v1 < v2 and v1 < v3:
    print(f"O menor valor é ${v1}")
elif v2 < v3 and v2 < v1:
    print(f"O menor valor é ${v2}")
if v3 < v1 and v3 < v2:
    print(f"O menor valor é ${v3}")

