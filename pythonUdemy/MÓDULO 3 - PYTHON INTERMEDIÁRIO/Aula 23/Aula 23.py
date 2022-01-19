"""
MÓDULO 3
AULA 23
GROUPBY
"""
from itertools import groupby
alunos = [
    {'nome': 'Marcos', 'nota': 'A'},
    {'nome': 'Michel', 'nota': 'B'},
    {'nome': 'Neto', 'nota': 'B'},
    {'nome': 'Marvin', 'nota': 'A'},
    {'nome': 'Samira', 'nota': 'D'},
    {'nome': 'Douglas', 'nota': 'A'},
    {'nome': 'Talyta', 'nota': 'C'},
    {'nome': 'Bianca', 'nota': 'B'},
    {'nome': 'Lucas', 'nota': 'A'},
    {'nome': 'Ana', 'nota': 'D'},
    {'nome': 'Carolina', 'nota': 'C'},
]
# ORGANIZA POR NOTA
alunos.sort(key=lambda item: item['nota'])
# AGRUPA POR NOTA
grupo = groupby(alunos, lambda item: item['nota'])
# CRIA OS TÍTULOS DOS GRUPOS (ABCD- TÍTULO)
# REDEFINE OS GRUPOS DE NOTAS COMO 'TABELA DE NOTAS'
for titulo, tabela_notas in grupo:
    print('GRUPO:', titulo)
    # DESEMPACOTA O GRUPO EM ITENS
    for item in tabela_notas:
        print(item)
    print()
