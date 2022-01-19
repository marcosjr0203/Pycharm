import math
#import pygame

# # Desafio 016 - Faça um programa que leia um número real e imprima apenas a parte inteira.
# n1 = float(input("Digite um número real: "))
# print(f"{math.floor(n1)}")


# # Desafio 017 - Crie um algoritmo que leia o comprimento dos catetos de um triângulo
# # retângulo, calcule e imprima a hipotenusa.
# n2 = float(input("Digite o valor do cateto adjacente: "))
# n3 = float(input("Digite o valor do cateto oposto: "))
# print(f"{math.sqrt(pow(n2,2)+pow(n3,2))}")

# # Desafio 018 - Desenvolva uma estrutura que leia um ângulo qualquer e imprima o seno,
# # coseno e tangente desse ângulo.
# n4 = int(input("Digite o ângulo desejado: "))
# print(f"Seno de {n4}º: {math.sin(n4):.2f}\nCoseno de {n4}º: {math.cos(n4):.2f}\n"
#       f"Tangente de {n4}º: {math.tan(n4):.2f}")


# # Desafio 019 - Faça um programa que leia nomes, sorteie e imprima um dentre estes.
# from random import choice
# n5 = input("Digite um nome: ")
# resp = input("Deseja digitar outro nome [y/n]?: ")
# lista = [n5]
# while resp == "y":
#     n6 = input("Digite outro nome: ")
#     lista += [n6]
#     resp = input("Deseja digitar outro nome [y/n]?: ")
# print(f"A lista completa dos nomes digitados é: ")
# for nome in lista:
#     print(nome)
# print(f"O nome sorteado foi: {choice(lista)}")

# # Desafio 020 - Crie um algoritmo que sorteie 'x' nomes e os imprima na ordem sorteada.
# from random import choice
# n7 = input("Digite um nome: ")
# resp = input("Deseja digitar outro nome [y/n]?: ")
# lista = [n7]
# while resp == "y":
#     n8 = input("Digite outro nome: ")
#     lista += [n8]
#     resp = input("Deseja digitar outro nome [y/n]?: ")
# print(f"A lista completa dos nomes digitados é: ")
# for nome in lista:
#     print(nome)
# sorteados = []
# c = 1
# nn = int(input(f"Digite quantos nomes deseja sortear: "))
# while c <= nn:
#     sorteia = choice(lista)
#     sorteados.append(sorteia)
#     c += 1
# d = 1
# for nome in sorteados:
#     while d <= nn:
#         print(f"O {d}º nome sorteado foi: {sorteados[d-1]}")
#         d += 1

# Desafio 021 - Desenvolva uma estrutura que leia um arquivo em mp3.
from pygame import mixer
mixer.init()
mixer.music.load('Thunderstruck.mp3')
mixer.music.play()
input()

