"""
EXERCÍCIOS DE REVISÃO (https://wiki.python.org.br/ListaDeExercicios)
1 - ESTRUTURA SEQUENCIAL
A) LOJA DE TINTAS
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe
ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
from math import ceil

mts = int(input('Digite o tamanho da área a ser pintada, em m²: '))
lata = mts/54
if lata > 1:
    print(f'Você precisará comprar {ceil(lata)} latas de tinta.\nValor total R$ {ceil(lata)*80},00.')
else:
    print('Você precisará de apenas 1 lata. Valor total R$ 80,00')