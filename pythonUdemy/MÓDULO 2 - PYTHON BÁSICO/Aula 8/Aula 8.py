"""
MÓDULO 2 - PYTHON BÁSICO
AULA 8
REVISÃO
"""

# EXERCÍCIO 003

"""
1 - CRIAR VARIÁVEIS PARA NOME (str), IDADE (int), ALTURA (float) E PESO (float) DE UMA PESSOA;
2 - CRIAR VARIÁVEL COM O ANO ATUAL (int);
3 - OBTER O ANO DE NASCIMENTO DA PESSOA (BASEADO NA IDADE E NO ANO ATUAL);
4 - OBTER O IMC DA PESSOA COM DUAS CASAS DECIMAIS;
5 - EXIBIR O TEXTO COM TODOS OS VALORES NA TELA USANDO F-STRINGS{}
"""
nome = 'Juca'
idade = 32
altura = 1.75
peso = 83.7
ano_atual = 2021
ano_nasc = ano_atual-idade
imc = peso/altura**2
print('{n} tem {i} anos, tendo nascido em {an}.\n{n} pesa {p} quilos, tem {al} metro de altura.\nO IMC de {n} é {im:.2f}'.format(n=nome, i=idade, an=ano_nasc, p=peso, al=altura, im=imc))
