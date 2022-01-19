"""
MÓDULO 3
AULA 32
CRIANDO PACOTES E MÓDULOS
"""
import vendas.calcula_precos
preco = 49.90
print(f'Valor: R$ {preco:.2f}')
aumento = vendas.calcula_precos.aumento(preco, 15)
print(f'Reajuste (15%): R$ {aumento-preco:.2f}')
reducao = vendas.calcula_precos.desconto(preco, 5)
print(f'Desconto (5%): R$ {preco-reducao:.2f}')
imposto =
vendas.calcula_precos.taxas(preco, 35)
print(f'Taxas e impostos: R$ {imposto-preco:.2f}')
print(f'Valor total: R$ {imposto-preco+preco-reducao+imposto-preco+preco:.2f}')

