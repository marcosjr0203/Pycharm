"""
MÓDULO 3
AULA 22
COMBINATIONS, PERMUTATIONS E PRODUCT - ITERTOOLS
COMBINATIONS - FORA DE ORDEM, SEM REPETIÇÃO DE VALORES ÚNICOS
PERMUTATIONS - EM ORDEM, SEM REPETIÇÃO DE VALORES ÚNICOS
PRODUCT - EM ORDEM, COM REPETIÇÃO VALORES ÚNICOS
"""
# # COMBINAÇÕES
# from itertools import combinations
# lista = [
#     'Marcos', 'Samira',
#     'Neto', 'Marvin',
#     'Michel'
# ]
# for duplas in combinations(lista, 2):
#     print(duplas)

# # PERMUTAÇÕES
# from itertools import permutations
# lista = [
#     'Marcos', 'Samira',
#     'Neto', 'Marvin',
#     'Michel'
# ]
# for duplas in permutations(lista, 2):
#     print(duplas)


# PRODUTO
from itertools import product
lista = [
    'Marcos', 'Samira',
    'Neto', 'Marvin',
    'Michel'
]
for duplas in product(lista, repeat=2):
    print(duplas)