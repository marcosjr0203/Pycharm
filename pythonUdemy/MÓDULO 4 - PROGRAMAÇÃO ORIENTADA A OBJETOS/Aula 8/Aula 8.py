"""
MÓDULO 4
AULA 8
RELAÇÃO ENTRE CLASSES
AGREGAÇÃO
"""
from Classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras
produto = Produto

p1 = Produto('Camiseta', 50)
p2 = Produto('Caneca', 30)
p3 = Produto('Celular', 2.550)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)

carrinho.lista_produtos()
print(carrinho.soma_total())
