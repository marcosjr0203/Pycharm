"""
MÓDULO 3
AULA 15
DICTIONARY COMPREHENSION
"""
lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

# d1 = {x: y for x, y in lista}
# # OU
# d1 = dict(lista)
# print(d1)

d1 = {f'chave{x}': x**2 for x in range(5)}
print(d1)