"""
MÓDULO 4
AULA 9
RELAÇÃO ENTRE CLASSES
COMPOSIÇÃO
"""
from Classes import Cliente, Endereco

c1 = Cliente('Marcos', 42)
c1.insere_endereco('Liverpool', 'UK')
print(c1.nome)
c1.lista_endereco()
print()

c2 = Cliente('Samira', 43)
c2.insere_endereco('Campo Grande', 'MS')
c2.insere_endereco('Liverpool', 'UK')
print(c2.nome)
c2.lista_endereco()
print()

c3 = Cliente('Marcos Neto', 20)
c3.insere_endereco('Campinas', 'SP')
print(c3.nome)
c3.lista_endereco()
print()


c4 = Cliente('Michel', 22)
c4.insere_endereco('Guaratinguetá', 'SP')
print(c4.nome)
c4.lista_endereco()
print()
print(f'{"":#^20}')

