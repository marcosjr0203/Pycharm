"""
MÓDULO 4
AULA 14
POLIMORFISMO
POLIMORFISMO É O PRINCÍPIO QUE PERMITE QUE CLASSES DERIVADAS
DE UMA MESMA SUPERCLASSE TENHAM MÉTODOS IGUAIS (DE MESMA
ASSINATURA - MESMO TIPO OU QUANTIDADE DE PARÂMETROS)
MAS COMPORTAMENTOS DIFERENTES
"""
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self,msg): pass


class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')

class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()
b.fala("Mensagem 1")
c.fala("Mensagem 2")