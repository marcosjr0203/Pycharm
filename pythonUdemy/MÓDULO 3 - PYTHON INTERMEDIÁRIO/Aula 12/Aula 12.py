"""
MÓDULO 3
AULA 12
EXERCÍCIO
- CRIAR UMA LISTA COM OUTRAS LISTAS DE NÚMEROS INTEIROS,
DE 10 ELEMENTOS CADA, CUJOS ELEMENTOS SEJAM NUMERAIS
ENTRE 0 E 9, PODENDO SER DUPLICADOS.

EXERCÍCIO:
- CRIAR UMA FUNÇÃO QUE ENCONTRE OS DOIS PRIMEIROS NÚMEROS
DUPLICADOS NAS LISTAS INTERNAS.
* A ORDEM DOS NÚMEROS DUPLICADOS É CONSIDERADA A PARTIR DA
SEGUNDA OCORRÊNCIA:
    EX.:
        [1, 2, 3, (3), 2, 1]
        RETORNAR: 3

* SE NÃO ENCONTRAR NENHUM ITEM DUPLICADO, RETORNAR -1
"""
lista_de_listas = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [0, 2, 2, 1, 3, 5, 0, 5, 0, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [0, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
def encontra (lista_interna):
    check=set()
    primeiro = -1
    for num in lista_interna:
        if num in check:
            primeiro = num
            break
        check.add(num)
    return primeiro


for lista in lista_de_listas:
    print(lista, '→', encontra(lista))
