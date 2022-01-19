# # PARÂMETROS IDENTICOS ALUNO E CLIENTE
# class Cliente:
#     def __init__(self, nome, idade):
#         self.nome = nome  # REPETE EM ALUNO
#         self.idade = idade  # REPETE EM ALUNO
#
# class Aluno:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# HERANÇA DE UMA CLASSE
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cliente(Pessoa):
    pass

class Aluno(Pessoa):
    pass