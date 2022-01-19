"""
MÓDULO 3
AULA 25
FILTER
"""
from Dados import produtos, pessoas, lista
# Filtragem dos dados em 'lista'
lista_reduzida = filter(lambda x: x > 5, lista)
lista_reduzida = list(lista_reduzida)
print(lista_reduzida)
# Filtragem dos dados em 'pessoas'
menores = filter(lambda y: y['idade'] < 18, pessoas)
menores = list(menores)
print(menores)
# Filtragem dos dados em 'produtos'
mais_caros = filter(lambda z: z['preco'] > 20, produtos)
mais_caros = list(mais_caros)
print(mais_caros)

