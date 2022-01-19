"""
MÓDULO 4
AULA 15
CRIANDO EXCEÇÕES
"""


class ErroError(Exception):
    pass


def teste ():
    raise ErroError('Errado!')

try:
    teste()
except ErroError as error:
    print(f'Erro: {error}')