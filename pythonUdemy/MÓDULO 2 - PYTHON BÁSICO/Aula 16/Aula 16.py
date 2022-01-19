"""
MÓDULO 2 - PYTHON BÁSICO
AULA 16
EXERCÍCIOS PROPOSTOS
1 - FAÇA UM PROGRAMA QUE PEÇA AO USUÁRIO PARA DIGITAR UM NÚMERO INTEIRO,
INFORME SE ESTE NÚMERO É PAR OU ÍMPAR, CASO O USUÁRIO NÃO DIGITE UM NÚMERO
INTEIRO, INFORME QUE NÃO É UM NÚMERO INTEIRO.

2 - FAÇA UM PROGRAMA QUE PERGUNTE A HORA AO USUÁRIO E, BASEANDO-SE NO HORÁRIO
DESCRITO, EXIBA A SAUDAÇÃO APROPRIADA.

3 - FAÇA UM PROGRAMA QUE PEÇA O PRIMEIRO NOME DO USUÁRIO. SE O NOME TIVER 4 LETRAS
OU MENOS ESCREVA "SEU NOME É CURTO"; SE TIVER ENTRE 5 E 6 LETRAS, ESCREVA " SEU NOME
É NORMAL"; SE MAIOR DO QUE 6 LETRAS, ESCREVA "SEU NOME É MUITO GRANDE".
"""
# 1
num = input('Digite um número: ')
if str.isnumeric(num):
    print('O valor digitado é um número inteiro.')
    if int(num) % 2 == 0:
        print('Este número é par')
    else:
        print('Este número é ímpar')
else:
    print('O valor digitado não é um número inteiro.')

# 2
hora = input('Digite a hora atual (00-23): ')
if str.isnumeric(hora):
    if 5 < int(hora) < 12:
        print('Bom dia')
    elif 12 < int(hora) < 18:
        print('Boa tarde')
    elif 18 < int(hora) < 24:
        print('Boa noite')
    else:
        print('Boa madrugada')
else:
    print('O valor digitado é inválido')

# 3
nome = input('Qual é o seu primeiro nome? ')
num = len(nome)
print(f'Seu nome tem {num} letras.')
if num <= 4:
    print('Seu nome é curto')
elif 4 < num <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')