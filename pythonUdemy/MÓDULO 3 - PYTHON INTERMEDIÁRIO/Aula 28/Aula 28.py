"""
MÓDULO 3
AULA 28
LEVANTANDO EXCEÇÕES (RAISE)
"""


# def divide(n1, n2):
#     try:
#         return n1/n2
#     except ZeroDivisionError as error:
#         print('Adicionado no arquivo de LOG:', error)
#         raise
#
# try:
#     print(divide(2, 0))
# except ZeroDivisionError as error:
#     print('Erro: Não é possível efetuar divisão por 0 ')

try:
    cpf = input('Digite seu CPF: ')
    if len(cpf) != 11:
        raise ValueError('11 dígitos')
    print('Log')
except ValueError:
    print('Erro: O CPF deve conter 11 dígitos.')

