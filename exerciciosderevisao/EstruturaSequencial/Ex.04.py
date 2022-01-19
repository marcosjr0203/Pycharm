"""
TODO 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
c = 1
n = 0
ng = int(input("How many grades you want to get the average?\n"))
while c <= ng:
    n += float(input(f"Insert the {c}st grade: "))
    c += 1
print(f"Average: {float(n / ng)}")