"""
MÓDULO 3
AULA 21
COUNT - CONTADORES INFINITOS
"""
from itertools import count

# contador = count()
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
#

# contador2 = count(start=20, step=4)
# print(next(contador2))
# print(next(contador2))
# print(next(contador2))
# print(next(contador2))
# print(next(contador2))
# print(next(contador2))
# print(next(contador2))

anos = range(1983, 2021)
lista = list(anos)
contador = count()
minhavida = []
for a in lista:
    minhavida += [
        f'{next(contador)}'
        f' - {a + 1}'
    ]
print(minhavida)