"""
MÓDULO 3
AULA 5
FUNÇÕES 'DEF' PARTE 4
"""
variavel = 'valor'  # escopo global, exibida se for feito 'print'
#
#
# def func():
#     print(variavel)
#
#
# def func2():
#     variavel = 'valor 2'
#     print(variavel)
#
#
# func()
# func2()
#
# print(variavel)


# def func():
#     print(variavel)
#
#
# def func2():
#     global variavel
#     variavel = 'valor 2'
#     print(variavel)
#
#
# func()
# func2()
#
# print(variavel)

# def func():
#     print(variavel)
#
#
# def func2(arg=None):
#     arg = 'valor 2'
#     return arg
#
#
# variavel2 = func2()
# print(variavel2)

# ERRADO:
# def func():
#     print(variavel)
#     variavel = 1234
#     print(variavel)
# func()

# CORRETO:
# def func():
#     variavel = 1234
#     print(variavel)
# func()

# ERRADO:
# def func():
#     variavel2 = 1234
#     print(variavel2)
#
#
# def func2():
#     print(variavel2)
#
# func()

# CORRETO:
def func():
    variavel2 = 1234
    return (variavel2)


def func2(arg):
    print(arg)

var = func()
func2(var)
