"""
TODO 7. Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
n3 = int(input("Insira o terceiro valor: "))
if n1 != n2 != n3 != n2 != n1 != n3:
    if n1 > n2 and n1 > n3:
        if n2 > n3:
            print(f"O maior número é {n1} e o menor é {n3}")
        if n3 > n2:
            print(f"O maior número é {n1} e o menor é {n2}")
    elif n2 > n1 and n2 > n3:
        if n1 > n3:
            print(f"O maior número é {n2} e o menor é {n3}")
        if n3 > n1:
            print(f"O maior número é {n2} e o menor é {n1}")
    elif n3 > n1 and n3 > n2:
        if n1 > n2:
            print(f"O maior número é {n3} e o menor é {n2}")
        if n2 > n1:
            print(f"O maior número é {n3} e o menor é {n1}")
else:
    print("Os valores devem ser diferentes.")

