"""
MÓDULO 2 - PYTHON BÁSICO
AULA 13
QUANTIDADE DE CARACTERES
LEN
"""
usuario = input('Nome de usuário: ')
qtd_caracteres = len(usuario)
# if qtd_caracteres < 8:
#     print('O nome de usuário precisa ter ao menos 8 caracteres.')
# else:
#     print('Usuário cadastrado com sucesso!')
print(qtd_caracteres)
print(usuario.__len__())


# nome = input('Digite seu nome: ')
# sobrenome = input('Digite seu sobrenome: ')
# numletras = len(nome)+len(sobrenome)
# print(f'Seu nome e sobrenome juntos possuem {numletras} letras.')
