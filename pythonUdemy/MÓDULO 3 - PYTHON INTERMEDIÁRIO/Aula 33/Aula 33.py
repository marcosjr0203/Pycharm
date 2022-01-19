"""
MÓDULO 3
AULA 33
CRIANDO, LENDO ESCREVENDO E APAGANDO ARQUIVOS
https://docs.python.org/3/library/functions.html#open
"""
# # ABERTURA DE ARQUIVO PARA LER E ESCREVER:
# file = open('nome.txt', 'w+')
# file.write('Linha1\n')
# file.write('Linha2\n')
# file.write('Linha3\n')
# file.close()
#
# # ABERTURA DE ARQUIVO PARA LEITURA:
# file = open('nome.txt')
# file.seek(0, 0)
# print(file.read())
# file.close()

# # LEITURA DE UMA LINHA:
# file = open('nome.txt')
# file.seek(0, 0)
# print(file.readline(), end='')
# print(file.readline())
# file.close()

# # LEITURA DE VÁRIAS LINHAS:
# file = open('nome.txt')
# file.seek(0, 0)
# for linha in file.readlines():
#     print(linha, end='')
# file.close()

# # UTILIZANDO ‘TRY’ PARA LEITURA DE ARQUIVOS
# try:
#     file = open('nome.txt', 'w+')
#     file.write('Linha')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()

# # GERENCIADOR DE CONTEXTO
# with open('nome.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#
#     file.seek(0)
#     print(file.read())
#
# # R+ MODO LEITURA
# with open('nome.txt', 'r') as file:
#     print(file.read())
#
# # A+ MODO 'APPEND'
# with open('nome.txt', 'a+') as file:
#     file.write('Outra Linha')
#     print(file.read())

# APAGANDO ARQUIVO
# import os
# os.remove('nome.txt')

# # MÓDULO JSON
# import json
#
# d1 = {
#     'pessoa 1': {
#         'nome': 'Samira',
#         'idade': 38,
#
#     },
#     'pessoa 2': {
#         'nome': 'Marcos',
#         'idade': 37,
#     },
# }
# d1_json = json.dumps(d1)
# print(d1_json)

# # CRIANDO UM ARQUIVO JSON
# with open('nome.json', 'w+') as file:
#     file.write('d1_json')
#
# # LENDO UM ARQUIVO JSON
# with open('nome.json', 'r') as file:
#     print('d1_json')

# CONVERTENDO UM ARQUIVO JSON EM UM DICIONÁRIO
with open('nome.json', 'r') as file:
    d1_json = file.read()
    d1_json = file.loads(d1_json)

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)