"""
MÓDULO 3
AULA 11
CONJUNTOS
ADD - ADIÇÃO
UPDATE - ATUALIZAÇÃO
CLEAR - LIMPEZA
DISCARD - DESCARTE
UNION | - UNIÃO DOS SETS
INTERSECTION & - ELEMENTOS DE AMBOS OS SETS
DIFFERENCE - ELEMENTOS APENAS NO SET DA ESQUERDA
SYMMETRIC_DIFFERENCE ^ - ELEMENTOS EM AMBOS OS SETS
"""
# set1 = {1, 2, 3, 4, 5}
# print(type(set1))
# for valor in set1:
#     print(valor)

# # ADD
# set2 = set()
# set2.add('a')
# set2.add('b')
# set2.add('c')
# set2.add('d')
# print(set2)

# # UPDATE
# set3 = set()
# set3.update('ABCDEF')
# print(set3)
# # CLEAR
# set3.clear()
# print(set3)

# # DISCARD
# set4 = {'A1', 'B2', 'C3', 'D4', 'E5', }
# print(set4)
# set4.discard('B2')
# print(set4)

# # UNION
# set5 = {'A1', 'B2', 'C3', 'D4', 'E5', }
# set6 = {98, 65, 32, 87}
# set7 = set5 | set6
# print(set7)

# # INTERSECTION
# set8 = {73, 56, 29, 87}
# set9 = {98, 65, 32, 87}
# set10 = set8 & set9
# print(set10)

# # DIFFERENCE
# set11 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# set12 = {3, 4, 5, 6, 7, 8, 9, 10, 11}
# set13 = set11 - set12
# print(set13)

# # SYMMETRIC DIFFERENCE
# set14 = {1, 2, 3, 4, 4, 5, 6, 7, 8, 9}
# set15 = {3, 4, 5, 6, 7, 8, 9, 10, 11}
# set16 = set14 ^ set15
# print(set16)

# NÃO DUPLICIDADE
set17 = {'joão', 'adriano', 'francisco', 'genésio' }
set18 = {'joão', 'marcos', 'luiz', 'adriano', 'paulo'}
set19 = set17 | set18
print(set19)
