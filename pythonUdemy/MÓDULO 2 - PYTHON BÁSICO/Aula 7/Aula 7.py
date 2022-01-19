"""
MÓDULO 2 - PYTHON BÁSICO
AULA 7
FORMATAÇÃO DE STRINGS (fstrings)
"""
nome = 'João'
idade = 28
altura = 1.76
peso = 75.3
imc = peso/altura**2
"""STRING NORMAL"""
print(nome, 'possui', idade, 'anos de idade e seu IMC é ', imc)
"""FSTRING"""
print(f'{nome} possui {idade} anos de idade e seu IMC é {imc:.2f}')
print('{} possui {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('A idade de {n} é {i}. O IMC de {n} é {c}. {n} possui {i} anos de idade e seu imc é {c}'.format(n=nome, i=idade, c=imc))
