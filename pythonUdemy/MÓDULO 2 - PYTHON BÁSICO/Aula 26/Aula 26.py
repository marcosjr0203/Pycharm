"""
MÓDULO 2 - PYTHON BÁSICO
AULA 26
DESEMPACOTAMENTO DE LISTAS
"""
# lista = ['Luiz', 'João', 'Maria']
# n1, n2, n3 = lista
# print(lista)
# print(n2)

# lista = ['Luiz', 'João', 'Maria', 'Joana', 'Nelson', 'Júlia']
# n1, n2, *demais_itens = lista
# print(n1)
# print(n2)
# print(demais_itens)
#
# lista = ['Luiz', 'João', 'Maria', 'Joana', 'Nelson', 'Júlia']
# n1, n2, *demais_itens, ultimo = lista
# print(ultimo)

lista = ['Luiz', 'João', 'Maria', 'Joana', 'Nelson', 'Júlia']
*demais_itens, n1, n2, ultimo = lista
print(demais_itens, n2)
