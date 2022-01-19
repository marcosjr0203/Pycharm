"""
MÓDULO 4
AULA 10
HERANÇA SIMPLES
ASSOCIAÇÃO - OBJETOS USAM OUTROS (MUITOS PARA MUITOS)
AGREGAÇÃO - UM OBJETO AGREGA OUTROS (UM PARA MUITOS)
COMPOSIÇÃO - UM OBJETO CONTÉM OUTROS (MUITOS EM UM)
HERANÇA - UM OBJETO É OUTRO (UM TORNA-SE OUTRO)
"""
from Classes import *
c1 = Cliente('Samira', 38)
print(f'Nome: {c1.nome}, idade: {c1.idade}')
c2 = Cliente('Marcos', 37)
print(f'Nome: {c2.nome}, idade: {c2.idade}')
a1 = Aluno('Michel', 17)
print(f'Nome: {a1.nome}, idade: {a1.idade}')
a2 = Aluno('Marcos Neto', 16)
print(f'Nome: {a2.nome}, idade: {a2.idade}')
a3 = Aluno('Marvin', 4)
print(f'Nome: {a3.nome}, idade: {a3.idade}')


