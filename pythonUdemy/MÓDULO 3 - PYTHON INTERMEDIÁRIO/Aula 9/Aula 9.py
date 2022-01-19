"""
MÓDULO 3
AULA 9
DICIONÁRIOS
"""
# dicionario = dict(chave='valor')
# dicionario['chave2'] = 'acréscimo1'
# dicionario['chave3'] = 'acréscimo2'
# dicionario['chave4'] = 'acréscimo3'
# dicionario['chave5'] = 'acréscimo4'
# dicionario['chave6'] = 'acréscimo5'
# print(dicionario)

# dicionario = dict(chave='valor')
# dicionario['chave2'] = 'acréscimo1'
# dicionario['chave3'] = 'acréscimo2'
#
# if 'acréscimo3' not in dicionario:
#     dicionario['chave4'] = 'acréscimo3'
#
# print(dicionario)

# dicionario = dict(chave='valor')
# dicionario['chave2'] = 'acréscimo1'
# dicionario['chave3'] = 'acréscimo2'
# dicionario['chave4'] = 'acréscimo3'
# dicionario['chave5'] = 'acréscimo4'
# dicionario['chave6'] = 'acréscimo5'
# print(dicionario.get('chave3'))
# print(dicionario('acréscimo3'))

# dicionario = dict(chave='valor')
# dicionario['chave2'] = 'acréscimo1'
# dicionario['chave3'] = 'acréscimo2'
# dicionario['chave4'] = 'acréscimo3'
# del dicionario['chave3']
# print(dicionario)

dicionario = dict(chave='valor')
dicionario['chave2'] = 'acréscimo1'
dicionario['chave3'] = 'acréscimo2'
dicionario['chave4'] = 'acréscimo3'
print('chave' in dicionario)
print('chave' in dicionario.keys())
print('acréscimo' in dicionario.values())