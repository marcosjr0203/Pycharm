"""
MÓDULO 4
AULA 13
CLASSES ABSTRATAS
"""
# from abc import ABC, abstractmethod
#
#
# class pessoa(ABC):
#     @abstractmethod
#     def falar(self):
#         pass
#
#
# class Marcos(pessoa):
#     def falar(self):
#         print('Marcos falando...')
#
# class Samira(pessoa):
#     def falar(self):
#         print('Samira falando...')
#
# a = Marcos()
# b = Samira()
# a.falar()
# b.falar()
# c = pessoa()
# c.falar()

from Classes.cp import ContaPoupanca

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)