"""
MÓDULO 3
AULA 20
EXERCÍCIO
SOMANDO DUAS LISTAS
Considerando duas listas de integers ou floats (A e B),
some os valores nas listas retornando uma nova lista com
os valores somados:

se uma lista for maior que outra, ssoma só vai considerar
o tamanho da lista menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
soma_ab = [2, 4, 6, 8]
"""
lista_a = [7, 12, 14, 8, 19, 2, 36]
lista_b = [21, 36, 15, 9, 86]
soma_ab = zip(lista_a, lista_b)
# MODO 1
lista_soma = []
for item in range(len(lista_b)):
    lista_soma.append(lista_a[item] + lista_b[item])
    print(lista_soma)

# MODO 2
lista_soma = []
for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i] + lista_b[i])
    print(lista_soma)

# MODO 3
for soma in soma_ab:
    print(soma[0]+soma[1])

# MODO 4
soma = [x + y for x,y in zip(lista_a, lista_b)]
print(soma)
