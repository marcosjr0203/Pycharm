"""
MÓDULO 3
AULA 36
PROBLEMA DOS PARÂMETROS MUTÁVEIS EM FUNÇÕES
"""


def lista_clientes(iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(iteravel)
    return lista


clientes1 = lista_clientes(['João', 'Maria', 'Gustavo'])
clientes2 = lista_clientes(['Fabiana', 'Nelson', 'Inah'])

print(clientes1)
print(clientes2)