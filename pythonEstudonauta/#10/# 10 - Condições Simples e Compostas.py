# # Desafio 028 - Escreva um programa em que o usuário tente adivinhar um número entre 0 e 5:
# from random import randint
# sort = randint(0, 5)
# guess = input("Estou pensando em um número entre 0 e 5, tente adivinhá-lo: ")
# game_over = False
# while not game_over:
#     if guess.isnumeric():
#         if 0 <= int(guess) <= 5:
#             if int(guess) == sort:
#                 print("Adivinhou!")
#                 game_over = True
#             else:
#                 guess = input("Errou... Tente de novo: ")
#         else:
#             guess = input("O Valor está entre 0 e 5, tente novamente: ")
#     else:
#         guess = input("O valor digitado deve ser um número entre 0 e 5, tente de novo: ")
#
# # Desafio 029 - Escreva um programa que leia a velocidade de um carro e o multe em R$ 7,00 se estiver acima de 80km/h:
# vel = input("Insira a velocidade: ")
# if vel > 80:
#     print("Você foi multado em R$ 7,00")
# else:
#     print("Você está na velocidade permitida. Boa viagem.")
# Desafio 030 - Escreva um programa que leia um número inteiro e mostre se ele é par ou ímpar:
# num = input("Digite um número: ")
# while not num.isnumeric():
#     num = input("Digite um número inteiro: ")
# if num.isnumeric():
#     num = int(num)
#     if num % 2 == 0:
#         print("Número par.")
#     else:
#         print("Número ímpar.")

# # Desafio 031 - Escreva um programa que pergunte a distância de uma viagem (km), calcule o preço da passagem, sendo:
# # R$ 0,50/km - se viagens de até 200km e R$ 0,45/km - se viagens de acima de 200km
# dist = input("Digite a distância, em KM: ")
# while not dist.isnumeric():
#     dist = input("Valor inválido. Digite um número inteiro arrendondando para menos, se houver decimais: ")
# if dist.isnumeric():
#     dist = int(dist)
#     if dist > 200:
#         val = 0.45
#         print(f"Valor da passagem: R$ {val*dist:.2f}")
#     else:
#         val = 0.5
#         print(f"Valor da passagem: R$ {val*dist:.2f}")
# # Desafio 032 - Escreva um programa que mostre se um ano é bissexto:
# # 01
# ano = input("Digite um ano: ")
# while not ano.isnumeric():
#     ano = input("Digite um valor numérico, sem separações por ponto ou vírgula: ")
# if ano.isnumeric():
#     ano = int(ano)
# if ano % 400 == 0:
#     print("Ano bissexto.")
#     if ano % 100 != 0:
#         print("Ano bissexto.")
#         if ano % 400 == 0:
#             print("Ano bissexto.")
#         else:
#             print("Ano não bissexto.")
#     else:
#         print("Ano não bissexto")
# else:
#     print("Ano não bissexto")
#
# # 02
# ano = int(input())
# if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
#     print('Ano bissexto.')
# else:
#     print('Não é um ano bissexto.')

# # Desafio 033 - Escreva um programa que leia 3 números e mostre o maior e o menor:
# r = "s"
# lista = []
# while r == "s":
#     num = input("Digite um número: ")
#     if num.isnumeric():
#         num = int(num)
#     else:
#         num = input("Digite um número válido: ")
#         num = int(num)
#     lista.append(num)
#     r = input("Deseja continuar? [S/N]: ")
# print("Itens por ordem de digitação:")
# for item in lista:
#     print(item)
# print("Itens por ordem crescente:")
# lista = sorted(lista)
# for item in lista:
#     print(item)

# # Desafio 034 - Escreva um programa que pergunte o salário de um funcionário e calcule um aumento, sendo:
# # 10% para salários superiores a 1.250,00
# # 15% para salários inferiores a 1.250,00
# sal = input("Digite o salário: ")
# if sal.isnumeric():
#     sal = int(sal)
# if sal > 1250:
#     sal = sal*1.1
# else:
#     sal = sal*1.15
# print(f"Seu novo salário é R$ {sal:.2f}.")

# Desafio 035 - Escreva um programa que receba o tamanho de 3 retas e informe se elas podem ou não formar um triângulo:
# Condição de existência de um triângulo:
# Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas
# dos outros dois e maior que o valor absoluto da diferença entre essas medidas.
# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b
# a = int(input("Digite o tamanho da 1ª reta: "))
# b = int(input("Digite o tamanho da 2ª reta: "))
# c = int(input("Digite o tamanho da 3ª reta: "))
# if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
#     print(f"{a}, {b} e {c} formam um triângulo")
# else:
#     print(f"{a}, {b} e {c} não formam um triângulo")

