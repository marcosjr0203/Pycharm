"""
MÓDULO 4
AULA 3
MÉTODOS ESTÁTICOS
"""
from random import randint


class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nasc(self):
        print(self.ano_atual - self.idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa('Marcos', 38)
print(Pessoa.gera_id())
print(p1.gera_id())