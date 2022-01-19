"""
MÓDULO 2 - PYTHON BÁSICO
AULA 12
OPERADORES LÓGICOS
AND, OR, NOT
IN E NOT IN
"""
nome = input("Nome:")
sobrenome = input('Sobrenome: ')
idade = int(input("Idade:"))
sexo = input("Sexo:")
letra = input("Busca-Letra: ")
if not nome or not idade or not sexo:
    print(f'Por favor, preencha todos os dados corretamente')
if letra in nome:
    print(f'{nome} tem a letra {letra}.')
else:
    print(f'Não tem a letra {letra} em {nome}.')
if letra not in sobrenome:
    print(f'nem em seu sobrenome existe a letra {letra}.')
if letra in sobrenome:
    print(f'Mas a letra {letra} está no seu sobrenome.')


nome = input("Usuário: ")
senha = input("Senha: ")
userbd = 'josedeoliveira'
senhabd = '12deoliveira3'
if userbd == nome and senha == senhabd:
    print('Bem Vindo!')
else:
    print('Usuário ou senha inválidos.')