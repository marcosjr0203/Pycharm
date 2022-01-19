"""
MÓDULO 3
AULA 24
FUNÇÃO 'MAP'
ARQUIVO ANEXO: DADOS
"""
from Dados import produtos, pessoas, lista
# print(lista)
# # FORMA USUAL
# mult2 = [v*2 for v in lista]
# print(mult2)
#
# # UTILIZANDO MAP
# mult22 = map(lambda x: x*2, lista)
# print(list(mult22))

# # MANIPULANDO DADOS COM "MAP"
# # Acrescentar 5% em cada produto da lista 'produtos':
# # Modo do aluno
# # 1 - Tirando a parte do preço da lista de produtos
# precos = map(lambda y: y['preco'], produtos)
# # 2 - Aplicando o aumento, usando apenas a lista de preços
# aumento = map(lambda x: x*1.05, precos)
# # 3 - Tornando o objeto 'aumento' uma lista
# lista_nova = list(aumento)
# # 4 - Configurando a exibição dos itens em 'lista_nova'
# for item in lista_nova:
#     item = f'R$ {item:.2f}'
#     print(item)

# # MANIPULANDO DADOS COM "MAP"
# # Acrescentar 5% em cada produto da lista 'produtos':
# # Modo do professor - manipulando diretamente na lista 'produtos'
#
#
# def reajuste(valor):
#     valor['preco'] = f'{valor["preco"]*1.05:.2f}'
#     return valor
#
#
# novos_precos = map(reajuste, produtos)
#
# for itens in novos_precos:
#     print(itens)

# MANIPULANDO DADOS COM "MAP"
# Tirar os nomes da lista 'pessoas' e criar nova idade para cada nome
# Modo do aluno
# 1 - Tirando a parte dos nomes da lista 'pessoas'
nomes = map(lambda x: x['nome'], pessoas)
# 2 - Tornando 'nomes' uma lista
lista_nova = list(nomes)
print(lista_nova)
# 3 - Criando nova idade


def new_age(aumento):
    aumento['idade'] = aumento['idade']+1
    return aumento


nova_idade = map(new_age, pessoas)
for nomes in nova_idade:
    print(nomes)