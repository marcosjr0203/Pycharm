# # Desafio 22 - Crie um programa que leia o nome completo de uma pessoa e o mostre:
# nome = input("Digite seu nome completo: ")
# # a) Com todas as letras em maiúsculo;
# print(nome.upper())
# # b) Com todas as letras em minúsculo;
# print(nome.lower())
# # c) Quantas letras possui, exceto espaços;
# print(f"Letras do nome completo, sem espaços: {len(nome)-nome.count(' ')}")
# # d) Quantas letras possui o primeiro nome;
# print(f"Letras no primeiro nome: {len(nome) - len(nome[nome.find(' '):])}")

# # Desafio 23 - Crie um programa que leia um número de 4 dígitos e os separe em unidade, dezena, centena e milhar:
# numero = input("Digite um número entre 1000 e 9999: ")
# if numero.isnumeric():
#     numero = int(numero)
#     while numero < 1000 or numero > 9999:
#         numero = int(input("Erro! O número deve estar entre 1000 e 9999.\nTente novamente: "))
#     numero = str(numero)
#     print(f"Milhar: {numero[0]}")
#     print(f"Centena: {numero[1]}")
#     print(f"Dezena: {numero[2]}")
#     print(f"Unidade: {numero[3]}")


# # Desafio 24 - Crie um programa que leia um nome de cidade e diga se começa ou não com "Santo"
# nome1 = input("Digite o nome de uma cidade qualquer: ")
# lista_nome = nome1.split(" ")
# print(f"O primeiro nome dessa cidade é {lista_nome[0]}")
# if "Santo" in nome1 or "São" in nome1 or "Santa" in nome1 or\
#         "Jesus" in nome1 or "Nossa" in nome1 or "Espírito" in nome1:
#     print(f"Essa cidade homenageia um santo.")
# else:
#     print(f"Essa cidade não homenageia nenhum santo.")


# # Desafio 25 - Crie um programa que leia um nome de pessoa e diga se possui ou não "Silva"
# nome2 = input("Digite um nome completo: ")
# if "Silva" in nome2:
#     print("Tem 'Silva' nesse nome")
# else:
#     print("Não tem 'Silva' nesse nome")

# Desafio 26 - Crie um programa que leia uma frase digitada pelo usuário e retorne:
frase = input("Digite uma frase qualquer: ").lower()
letra = input("Digite qual letra deseja buscar: ")
print(f"Essa frase possui {len(frase)} letras (incluindo espaços)")
# a) Quantas vezes certa letra aparece;
if frase.count(letra) <= 1:
    print(f"A letra {letra} aparece {frase.count(letra)} vez nesta frase")
else:
    print(f"A letra {letra} aparece {frase.count(letra)} vezes nesta frase")

# b) Em que posição ela aparece pela primeira vez;
print(f"A letra {letra} aparece pela primeira vez nesta frase"
      f" na {frase.find(letra) + 1}ª posição (incluindo os espaços).")
# c) Em que posição ela aparece pela última vez.
esarf = frase[::-1]
print(esarf)
ult = len(frase)-esarf.find(letra)
print(f"A letra {letra} aparece pela última vez nesta frase"
      f" na {ult}ª posição (incluindo os espaços).")

# # Desafio 27 - Crie um programa que leia o nome completo de uma pessoa e mostre em separado o primeiro e o último nome.
# nome3 = input("Digite seu nome completo: ")
# lista = nome3.split()
# print(f"Olá {lista[0]} {lista[len(lista)-1]}")

