"""
MÓDULO 3
AULA 17
COMPORTAMENTO DE GERADORES E ITERADORES
"""
nome = 'Marcos'
nome = iter(nome)
for letra in nome:
    print(letra)
print(next(nome))
print(next(nome))
print(next(nome))
print(next(nome))
print(next(nome))
print(next(nome))
print(next(nome))

