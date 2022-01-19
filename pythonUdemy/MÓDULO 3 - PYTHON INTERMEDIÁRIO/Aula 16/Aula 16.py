"""
MÓDULO 3
AULA 16
GERADORES, ITERADORES E ITERÁVEIS
"""
# # VERIFICANDO SE UM OBJETO É ITERÁVEL
# iteravel = [0, 1, 2, 3, 4, 5]
# print(hasattr(iteravel,'__iter__'))
# nao_iteravel = 1.984
# print(hasattr(nao_iteravel,'__iter__'))

# # ITERAÇÃO
# lista = [0, 1, 2, 3, 4, 5]
# for v in lista:
#     print(v)

# # VERIFICANDO SE UMA LISTA É UM ITERADOR
# lista = [0, 1, 2, 3, 4, 5]
# print(hasattr(lista, '__next__'))

# # TORNANDO UMA LISTA ITERÁVEL
# lista = [0, 1, 2, 3, 4, 5]
# lista = iter(lista)
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))

# # GERADORES
# import sys
#
# lista = list(range(1000000))
# print(sys.getsizeof(lista), 'bytes de memória utilizados')

# EXEMPLO DE UM SISTEMA SEM GERADOR
import time


def gera ():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r


g = gera()

for v in g:
    print(v)


# EXEMPLO DE UM SISTEMA COM GERADOR
import time


def gera ():
    r = []
    for n in range(100):
        yield n
        time.sleep(0.1)
    return r


g = gera()

for v in g:
    print(v)
