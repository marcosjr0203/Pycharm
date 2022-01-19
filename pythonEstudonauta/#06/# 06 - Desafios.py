# Desafio 003 - Crie um programa que some dois números e mostre a soma entre eles
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1 + n2
print(s)

# Desafio 004 - Crie um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo:
n = input("Digite algo: ")
print("É numérico? ", n.isnumeric())
print("É um dígito? ", n.isdigit())
print("É decimal? ", n.isdecimal())
print("É Alfanumérico? ", n.isalnum())
print("É Alfabético? ", n.isalpha())
print("É ASCII? ", n.isascii())
print("Possui iniciais em maiúsculo? ", n.istitle())
print("Possui todas as letras em minúsculo? ", n.islower())
print("Possui todas as letras em maiúsculo", n.isupper())
print("É uma string que contem apenas espaços? ", n.isspace())
print("É um identificador válido (para dar nome a uma variável)? ", n.isidentifier())


