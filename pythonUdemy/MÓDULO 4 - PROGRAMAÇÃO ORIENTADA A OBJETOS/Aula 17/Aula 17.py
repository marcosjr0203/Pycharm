"""
MÓDULO 4
AULA 17
MÉTODOS MÁGICOS
https://rszalski.github.io/magicmethods/
"""
# class A:
#     def __new__(cls, *args, **kwargs):
#         print("Eu sou NEW")
#         return object.__new__(cls)
#
#     def __init__(self):
#         print("Eu sou INIT")
#
# a = A()

# #PERSONALIZAÇÃO DA INSTÂNCIA EM 'NEW'
# class A:
#     def __new__(cls, *args, **kwargs):
#
#         def saudacao(*args, **kwargs):
#             print("Que a força esteja com você!")
#
#         cls.saudacao = saudacao
#         return object.__new__(cls)
#
#
# a = A()
# a.saudacao()


# MÉTODO __CALL__
class A:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        resultado = 1

        for i in args:
            resultado *= i
        return resultado


a = A()
valores = a(1, 2, 3, 4, 5)
print(f'Resultado: {valores}')


