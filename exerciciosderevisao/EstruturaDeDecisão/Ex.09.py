"""
TODO 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
n3 = int(input("Insira o terceiro valor: "))
ln = []
if n1 != n2 != n3 != n2 != n1 != n3:
    if n1 < n2 and n1 < n3:
        if n2 < n3:
            ln.append(n1)
            ln.append(n2)
            ln.append(n3)
        if n3 < n2:
            ln.append(n1)
            ln.append(n3)
            ln.append(n2)
    elif n2 < n1 and n2 < n3:
        if n1 < n3:
            ln.append(n2)
            ln.append(n1)
            ln.append(n3)
        if n3 < n1:
            ln.append(n2)
            ln.append(n3)
            ln.append(n1)
    elif n3 < n2 and n3 < n1:
        if n2 < n1:
            ln.append(n3)
            ln.append(n2)
            ln.append(n1)
        if n1 < n2:
            ln.append(n3)
            ln.append(n1)
            ln.append(n2)
    print(f"Ordem crescente: {ln}")


