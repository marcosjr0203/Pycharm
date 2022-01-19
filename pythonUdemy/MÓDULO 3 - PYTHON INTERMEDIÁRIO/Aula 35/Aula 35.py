"""
MÓDULO 3
AULA 3
FUNÇÕES DECORADORAS
"""
# def fala_oi():
#     print('Oi')
#
# variavel = fala_oi()

# # VARIÁVEL ASSUME VALOR DE FUNÇÃO
# def fala_oi():
#     print('Oi')
#
# variavel = fala_oi
# print(type(variavel))

# # FUNÇÃO ANINHADA EXECUTADA INTERNAMENTE
# def func_master():
#     def func_slave():
#         print('Hi')
#     func_slave()
#
# func_master()
#
# # FUNÇÃO ANINHADA NÃO EXECUTADA INTERNAMENTE
# def func_master():
#     def func_slave():
#         print('Hi')
#     return func_slave
#
# variavel = func_master
# print(type(variavel))

# # FUNÇÕES INTERLIGADAS
# def func_master(funcao):
#     def func_slave():
#         funcao()
#     return func_slave
#
#
# def fala_oi():
#     print('Oi')
#
#
# variavel = func_master(fala_oi)
# variavel()

# UTILIZANDO @ PARA DECORAÇÃO DE FUNÇÕES
def func_master(func):
    def func_slave():
        print('decorado')
    return func_slave


# @func_master
def fala_oi():
    print('Oi')


fala_oi()

