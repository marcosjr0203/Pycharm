"""
MÓDULO 4
AULA 4
@PROPERTY
GETTERS E SETTERS
"""
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))

    #GETTER
    @property
    def preco(self):
        return self._preco

    #SETTER
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = valor.replace('R$', '')

        self._preco = valor

prod1 = Produto('Camiseta', 50)
prod1.desconto(10)
print(f'R$ {prod1.preco}')

prod2 = Produto('Caneca', 'R$25')
prod2.desconto(10)
print(f'R$ {prod2.preco}')