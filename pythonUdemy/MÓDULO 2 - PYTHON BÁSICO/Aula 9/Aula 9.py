"""
MÓDULO 2 - PYTHON BÁSICO
AULA 9
ENTRADA DE DADOS DO USUÁRIO
"""
# EXEMPLO 1
# nome = input('Qual é o seu nome? ')
# idade = input('Qual a sua idade? ')
# peso = float(input('Qual é o seu peso? '))
# altura = float(input('Qual é a sua altura? '))
# print('Seu imc é ', peso/(altura**2))
# print('Agora, a variável "peso" é do tipo ', type(peso))
# print('A variável "altura" também é do tipo', type(altura))
"""
AO COLOCAR O INPUT PARA ENTRADA DE DADOS DO USUÁRIO, O SISTEMA SEMPRE O CONSIDERARÁ DO TIPO 'string'
NESTE EXEMPLO, PARA QUE NÃO HAJA ERRO NO CÁLCULO DE IMC, É NECESSÁRIO DECLARAR O TIPO 'float' DO INPUT
"""
# EXEMPLO 2
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print(n1 + n2)
# REMOVER AS HASHS (#) E ADICIONÁ-LAS NAS LINHAS DO EX.2 PARA EXECUTAR UM OU OUTRO EXEMPLO
