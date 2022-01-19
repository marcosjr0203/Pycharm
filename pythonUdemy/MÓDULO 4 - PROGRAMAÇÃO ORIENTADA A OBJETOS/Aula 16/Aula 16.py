"""
MÓDULO 4
AULA 16
SOBRECARGA DE OPERADORES
COMO ALTERAR O COMPORTAMENTO DE OPERADORES
COM CLASSES DEFINIDAS PELO USUÁRIO
"""


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<class'Retangulo({self.x, self.y})'>"

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)


r1 = Retangulo(10, 20)
r2 = Retangulo(20, 30)
r3 = r1 + r2
print(r3)