"""
MÓDULO 3
AULA 31
CRIANDO MÓDULOS
EXEMPLO DE MÓDULO
"""
from math import pi
PI = pi

def dobra(lista):
    return [x*2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r*=i
    return r


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(dobra(lista))
    print(multiplica(lista))
    print(PI)