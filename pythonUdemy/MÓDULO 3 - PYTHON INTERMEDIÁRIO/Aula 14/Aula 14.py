"""
MÓDULO 3
AULA 14
EXERCÍCIOS PROPOSTOS
"""
string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
contadores = [i for i in range (0, len(string), n)]
tuplas = [(i, i+n) for i in range(0, len(string), n)]
lista = [string[i:i+n]for i in range(0, len(string), n)]
raw = [f'string[{i}:{i + n}]' for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(contadores)
print(tuplas)
print(lista)
print(raw)
print(retorno)
