"""
MÓDULO 3 - PYTHON INTERMEDIÁRIO
AULA 2
FUNÇÕES 'DEF'
PARTE II
"""


def funcao(var):
    return (var)


variavel = funcao('Valor cadastrado.')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')

print('Digite 2 valores: ')
A = int(input('1º: '))
B = int(input('2º: '))


def operacao(n1, n2):
    if n2 > 0:
        return n1 / n2
    return print('Operação inválida')


    print(operacao(A, B))


def f(var):
    print(var)

def dumb():
    return f

var = dumb()('Inserido')
print(id(var), id(f))


# import turtle
#
# def desenhaQuadradoMulticolorido(t, tam):
#     """Faca a tartaruga t desenhar um quadrado multicolorido de lado tam."""
#     for i in ['red','purple','hotpink','blue']:
#         t.color(i)
#         t.forward(tam)
#         t.left(90)
#
# wn = turtle.Screen()              # Inicializa a janela e seus atributos
# wn.bgcolor("lightgreen")
#
# tess = turtle.Turtle()            # cria tess e seus atributos
# tess.pensize(3)
#
# tamanho = 20                      # tamanho do menor quadrado
# for i in range(15):
#     desenhaQuadradoMulticolorido(tess, tamanho)
#     tamanho = tamanho + 10       # aumenta o tamanho para a próxima vez
#     tess.forward(10)             # move tess um pouco à frente
#     tess.right(18)               # e dá uma virada nela
#
# wn.exitonclick()
