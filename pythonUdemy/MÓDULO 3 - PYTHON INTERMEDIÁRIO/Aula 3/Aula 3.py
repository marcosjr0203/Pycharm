"""
MÓDULO 3
AULA 3
EXERCÍCIOS PROPOSTOS
"""
"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""

# def cumprimento(msg='Olá', nome='Usuário'):
#     print(msg, nome)
#
#
# cumprimento('Bom dia', 'Marcos')
# cumprimento(msg='Boa tarde')
# cumprimento(nome='Marcos')
# cumprimento()

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre
eles.
"""
# print("Digite os valores abaixo: ")
# p = input('1º Valor: ')
# s = input('2º Valor: ')
# t = input('3º Valor: ')
# p, t, s = int(p), int(s), int(t)
#
#
# def soma(a=0, b=0, c=0):
#     return a + b + c
#
#
# print(soma(p, t, s))

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
# print("Digite os valores abaixo: ")
# p = int(input('Valor: '))
# s = int(input('% acréscimo: '))
#
#
# def percentual(a=0, b=0):
#     return a*(1+(b/100))
#
#
# print(percentual(p, s))

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.

"""
p = int(input('Digite um valor: '))


def fizzbuzz(valor=0):
    if valor % 3 == 0 and not valor % 5 ==0:
        return 'Fizz'
    elif valor % 5 == 0 and not valor % 5 ==0:
        return 'Buzz'
    elif valor % 3 == 0 and valor % 5 == 0:
        return 'FizzBuzz'
    else:
        print('Valor não divisível por 3 ou 5.')


print(fizzbuzz(p))
