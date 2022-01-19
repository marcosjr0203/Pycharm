"""
MÓDULO 3
AULA 4
FUNÇÕES 'DEF' PARTE 3
*args/**kwargs
"""


# def func(a, b, c, d, e, f, g=25, h=0, i=0, j=0):
#     print(a, b, c, d, e, f, g, h, i, j)
#
#
# func(1, 2, 3, d=0, e=0, f=0, g=0, h=0, i=0, j=0)


# def func(a, b, c):
#     return (a, b, c)
#
#
# var = func(1, 2, 3)
# print(var)


# lista = [1, 2, 3, 4, 5]
# print(lista)
# n1, n2, *n = lista
# print(n1, n2, n)
# print(*lista)

#
# def func(*args):
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
#
#
# func(1, 2, 3, 4, 5)


# def func(*args):
#     args = list(args)
#     args[0] = 20
#     print(args)
#
# func(1, 2, 3, 4, 5)

# def func(*args):
#     print(args)
#
#
# lista = [1, 2, 3, 4, 5]
# func(lista, 6)


# def func(*argumentos):
#     print(argumentos)
#
#
# lista = [1, 2, 3, 4, 5]
# func(*lista, 6)

def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value


# VALOR SEM DESCONTO
final_price = calculate_price(100.0)
print(final_price)


# VALOR COM DESCONTO
final_price = calculate_price(100.0, discount=5.0)
print(final_price)
