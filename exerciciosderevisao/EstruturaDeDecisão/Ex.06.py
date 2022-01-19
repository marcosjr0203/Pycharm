"""
TODO 6. Faça um Programa que leia três números e mostre o maior deles.
"""
n1 = int(input("Digite o 1º número inteiro: "))
n2 = int(input("Digite o 2º número inteiro: "))
n3 = int(input("Digite o 3º número inteiro: "))
if n1 > n2 and n1 > n3:
    print(f"O maior número é {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior número é {n2}")
elif n3 > n1 and n3 > n2:
    print(f"O maior número é {n3}")
elif n1 == n2 == n3:
    print("Os 3 valores são iguais.")
else:
    print("Os valores devem ser diferentes.")