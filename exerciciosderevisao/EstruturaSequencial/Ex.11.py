"""
TODO 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
10.1. o produto do dobro do primeiro com metade do segundo .
10.2. a soma do triplo do primeiro com o terceiro.
10.3. o terceiro elevado ao cubo.
"""
import time as t
i1 = int(input("Enter the first term, as an integer number: "))
i2 = int(input("Enter the second term, as another integer number: "))
f1 = float(input("Now, enter the third term, as a float number: "))
print(f"The product of the double of the first term with the half of the second term: {(2*i1)*(i2/2)}")
t.sleep(0.3)
print(f"The sum of the triple of the first term with the third term: {(3*i1)+f1}")
t.sleep(0.3)
print(f"The third term cubed: {(f1**3)}")
