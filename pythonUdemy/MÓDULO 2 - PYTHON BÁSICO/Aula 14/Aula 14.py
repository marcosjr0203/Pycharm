"""
MÓDULO 2 - PYTHON BÁSICO
AULA 14
DOCUMENTAÇÃO E FUNÇÕES BUILT-IN ÚTEIS
isnumeric, isdigit, isdecimal
https://docs.python.org/3/library/stdtypes.html
"""
import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


num1 = input('Digite um valor: ')
num2 = input('Digite outro valor: ')

if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)
    print('Soma: ', num1+num2)
else:
    print('Dados inválidos.')

try:
    num1 = float(input('Digite um valor: '))
    num2 = float(input('Digite outro valor: '))
    print('Soma: ', num1 + num2)
except:
    print('Dados inválidos.')

# if str.isnumeric(num1):
#     print('Num 1 é numérico')
# else:
#     print('Num 1 NÃO é numérico')
# if str.isdecimal(num1):
#     print('Num 1 é decimal')
# else:
#     print('Num 1 NÃO é decimal')
# if str.isdigit(num1):
#     print('Num 1 é dígito')
# else:
#     print('Num 1 NÃO é dígito')
