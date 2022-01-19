"""
MÓDULO 03
AULA 13
LIST COMPREHENSION
"""
l1 = [1, 2, 3, 4, 5]
print('l1:', l1)

# EXIBINDO ITENS
ex1 = [variavel for variavel in l1]
print('\nex1:', ex1)

# MULTIPLICANDO CADA ITEM POR 2
ex2 = [v * 2 for v in l1]
print('\nex2:', ex2)

# PAREANDO CADA ITEM COM UM VALOR DE 0 A 3 (RANGE)
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print('\nex3:', ex3)

# SUBSTITUINDO CARACTER EM UMA LISTA DE STRINGS
l2 = ['Maria', 'Mauro', 'Marcos']
ex4 = [v.replace('a','@').upper() for v in l2]
print('\nl2:', l2)
print('ex4:', ex4)

# INVERSÃO DE VALORES EM UMA TUPLA (OU LISTA)
tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex5 = [(y, x) for x, y in tupla]
print('\nex5:', ex5)

# SELECIONANDO MÚLTIPLOS DE UM NÚMERO
l3 = list(range(10))
print('\nl3:',l3)
ex6 = [v for v in l3 if v % 2 == 0]
print('ex6:',ex6)

# SELECIONANDO MÚLTIPLOS DE DOIS NÚMEROS
l4 = list(range(30))
print('\nl4:', l4)
ex7 = [v for v in l3 if v % 2 == 0 if v % 8 == 0]
print('ex7:', ex7)

# SELECIONANDO MÚLTIPLOS DE DOIS NÚMEROS COM 'ELSE'
l5 = list(range(36))
ex8 = [v if v % 2 == 0 and v % 3 == 0 else '*' for v in l5]
print('\nex8:', ex8)

