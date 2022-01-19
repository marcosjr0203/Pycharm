"""
MÓDULO 4
AULA 20
METACLASSES
"""
# # Definição
# class A: # Classe molde (metaclasse)
#     attr = 'Valor'
#
# a = A() # Objeto moldado por A
# b = A() # Objeto moldado por A
# c = A() # Objeto moldado por A

# # Sistema de classes
# class A:
#     def fala(self):
#         self.b_fala()
#
# class B(A):
#     def b_fala(self):
#         print ('Oi')
#
# b = B()
# b.fala()

# Forçando a criação de um método, com uma Metaclasse
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name =='A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f"É necessário criar o método 'b_fala' em {name}")
        else:
            if not callable(namespace['b_fala']):
                print(f"b_fala precisa ser um método, não atributo em {name}")

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()

class B(A):
    pass
    def sei_la(self):
        pass
b = B()
