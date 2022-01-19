"""
MÓDULO 4
AULA 2
MÉTODO DE CLASSES
"""


class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nasc(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nasc(cls, nome, ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade)


p1 = Pessoa('Marcos', 38)
print(p1)
print(p1.nome, p1.idade)
p1.ano_nasc()