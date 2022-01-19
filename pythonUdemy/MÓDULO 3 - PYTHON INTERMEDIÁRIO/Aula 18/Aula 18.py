"""
MÓDULO 3
AULA 18
EXERCÍCIO
"""
carrinho = []

carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', 20))
carrinho.append(('Produto3', 50))
print(carrinho)
total = sum([float(y) for x,y in carrinho])
print('Total:',total)