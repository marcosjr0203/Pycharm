"""
MÓDULO 2 - PYTHON BÁSICO
AULA 25
SPLIT, JOIN, ENUMERATE
* SPLIT: DIVIDE UMA STRING
* JOIN: JUNTA UMA LISTA DE STRINGS
* ENUMERATE: ENUMERA ELEMENTOS DE UMA LISTA DE STRINGS
"""
string = "O meu nome é Marcos"
lista = string.split(' ')
print(lista)

string = "Ontem, hoje, amanhã, sempre"
lista = string.split(',')
for valor in lista:
    print(f'{valor} → {lista.count(valor)}')

string = "O que é que você quer que eu faça?"
lista = string.split(' ')
palavra = ''
contagem = 0
for valor in lista:
    quant = lista.count(valor)
    if quant > contagem:
        contagem = quant
        palavra = valor
        print(f'A palavra "{palavra.lower()}" aparece {contagem} vezes na frase')

string = "Meu nome é Marcos"
lista = string.split(' ')
string2 = ' - '.join(lista)
print(string)
print(lista)
print(string2)

string = "Meu nome é Marcos"
lista = string.split(' ')
for indice, valor in enumerate(lista):
    print(indice, valor)

lista = [
    [1, 2],
    [3, 4],
    [5, 6],
]

for v in lista:
    (print(v[0], v[1]))