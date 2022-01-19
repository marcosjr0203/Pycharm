"""
TODO 3. Faça um Programa que peça dois números e imprima a soma.
"""
nt = int(input("How many terms do you want to sum?\n"))
ns = 0
while nt > 0:
    n = int(input(f"Insert the {nt}st term: "))
    ns += n
    nt = nt-1
print(ns)
print(f"The sum of the terms is {ns}")
