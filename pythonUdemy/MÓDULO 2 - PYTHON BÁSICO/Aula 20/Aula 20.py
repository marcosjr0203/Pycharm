"""
MÓDULO 2 - PYTHON BÁSICO
AULA 20
WHILEELSE - REPETIÇÃO COM ACUMULADORES
"""
acumulador = 1
contador = 1
while contador <= 10:
    print(contador, '\t→\t', acumulador)

    if contador > 3:
        break

    acumulador += contador
    contador += 1
else:
    print('Terminamos')
