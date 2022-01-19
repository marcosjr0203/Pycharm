"""
MÓDULO 3
AULA 19
ZIP E ZIP LONGEST
UNINDO ITERÁVEIS
"""
# # Código Cidade
# cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
#
# # Código Estado
# estados = ['SP', 'MG', 'BA', 'MG']
#
# # ZIP cidade + estado
# cidades_estado = zip(cidades, estados)
# for valor in cidades_estado:
#     print(valor[0], valor[1])
#

#DIFERENÇA ENTRE ZIP E UNION
# # União Cidade | Estado
# cidades_estados = set(cidades) | set(estados)
# print(cidades_estados)

#ZIP PARA CORRESPONDER ITENS (PELA MENOR LISTA)
# # Produto
# produtos = ['Banana', 'Maçã', 'Ameixa', 'Caju']
#
# # Preço
# precos = [6.99, 8.59, 10.99]
#
# # ZIP Produto + Preço
# produto_preco = zip(produtos, precos)
# for valor in produto_preco:
#     print(valor[0], valor[1])

# ZIP LONGEST PARA EXIBIR TODOS OS ITENS
# from itertools import zip_longest
# # Produto
# produtos = ['Banana', 'Maçã', 'Ameixa', 'Caju',
#             'Maracujá', 'Uva', 'Goiaba']
#
# # Preço
# precos = [6.99, 8.59, 10.99]
#
# # ZIP Produto + Preço
# produto_preco = zip_longest(produtos, precos, fillvalue=3.00)
# for valor in produto_preco:
#     print(valor[0], valor[1])

# USANDO UM CONTADOR IMPORTADO DA BIBLIOTECA ITERTOOLS
from itertools import zip_longest, count
# Contador
indice = count()
# Código Cidade
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

# Código Estado
estados = ['SP', 'MG', 'BA', 'MG']

# # ZIP cidade + estado
cidades_estado = zip(indice, cidades, estados)
for valor in cidades_estado:
    print(valor)

