"""
MÓDULO 3
AULA 25
REDUCE
"""
from Dados import produtos, pessoas, lista
from functools import reduce

# FORMA SIMPLES
total = 0
for n in lista:
    total += n
print(lista)
print(total)
# FORMA COM 'REDUCE'
total = reduce(lambda acumulador, y: acumulador + y, lista)
print(lista)
print(total)
