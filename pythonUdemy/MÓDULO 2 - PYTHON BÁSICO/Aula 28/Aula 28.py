"""
MÓDULO 2 - PYTHON BÁSICO
AULA 28
OPERAÇÃO TERNÁRIA
"""
logged_user = False
mensagem = 'Usuário logado.' if logged_user else 'Você precisa fazer login'
print(mensagem)

idade = (int(input('Qual sua idade: ')))
maioridade = (idade >= 18)
msg = 'Acesso permitido' if maioridade else 'Acesso não permitido'
print(msg)