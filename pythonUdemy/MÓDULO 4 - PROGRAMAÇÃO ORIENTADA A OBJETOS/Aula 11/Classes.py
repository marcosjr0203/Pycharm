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

# # HERANÇA DE UMA CLASSE
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#
# class Cliente(Pessoa):
#     pass
#
# class Aluno(Pessoa):
#     pass

# # SOBREPOSIÇÃO DE MEMBROS
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         self.nomeclasse = self.__class__.__name__
#
#     def falar(self):
#         print(f'{self.nomeclasse} falando...')
#
#
# class Cliente(Pessoa):
#     def comprar (self):
#         print(f'{self.nomeclasse} comprando...')
#
#
# class ClienteVip(Cliente):
#     def falar(self):
#         print(f'{self.nomeclasse} dizendo coisas...')
#
#
# class Aluno(Pessoa):
#     pass


# # SUPEREXECUÇÃO DE MÉTODOS COM 'SUPER()'
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         self.nomeclasse = self.__class__.__name__
#
#     def falar(self):
#         print(f'{self.nomeclasse} falando em Pessoa...')
#
#
# class Cliente(Pessoa):
#     def falar(self):
#         print(f'{self.nomeclasse} falando em Cliente...')
#
#
# class ClienteVip(Cliente):
#     def falar(self):
#         super().falar()
#         print(f'{self.nomeclasse} falando em ClienteVip...')

#
# # SUPEREXECUÇÃO DE MÉTODOS COM 'NOMEDACLASSE.MÉTODO()'
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         self.nomeclasse = self.__class__.__name__
#
#     def falar(self):
#         print(f'{self.nomeclasse} falando em Pessoa...')
#
#
# class Cliente(Pessoa):
#     def falar(self):
#         print(f'{self.nomeclasse} falando em Cliente...')
#
#
# class ClienteVip(Cliente):
#     def falar(self):
#         Pessoa.falar(self)
#         print(f'{self.nomeclasse} falando em ClienteVip...')
#

# SUBCONSTRUTORES (__INIT__)'
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando em Pessoa...')


class Cliente(Pessoa):
    def falar(self):
        print(f'{self.nomeclasse} falando em Cliente...')


class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')



