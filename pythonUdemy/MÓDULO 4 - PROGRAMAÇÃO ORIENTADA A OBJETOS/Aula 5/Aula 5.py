"""
MÓDULO 4
AULA 5
ATRIBUTOS DE CLASSE
"""
class A:
    vc = 123

# # CRIANDO NOVO ATRIBUTO PARA UMA VARIÁVEL DE CLASSE
# a1 = A()
# a2 = A()
#
# a1.vc = 321
# print(a1.vc)
# print(a2.vc)
# print(A.vc)

# TODAS AS VARIÁVEIS DE UMA CLASSE
a1 = A()
a2 = A()

A.vc = 321
print(a1.vc)
print(a2.vc)
print(A.vc)

