"""
Faça um Programa para uma loja de tintas.
1 - O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada.
2 - Considere que a cobertura da tinta é de 1 litro para cada 6 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam
R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
3 - Informe ao usuário as quantidades de tinta a serem compradas e os
respectivos preços em 3 situações:
* comprar apenas latas de 18 litros;
* comprar apenas galões de 3,6 litros;
* misturar latas e galões, de forma que o desperdício de tinta seja
menor.
* Acrescente 10% de folga e sempre arredonde os valores para
cima, isto é, considere latas cheias
"""
from math import ceil
tam = input('Digite o tamanho, em m² da área a ser pintada: ')
tam = float(tam)
tinta = tam/6*1.1
lg = ceil(tinta/18)
sobra = 0
print(f'Latas 18l :{lg}')
if tinta % 18 > 0:
    sobra = tinta-ceil(tinta/lg)
    print('Tinta excedente: ', sobra)
