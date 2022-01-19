"""
TODO 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
import math as m
pi = m.pi
r = float(input("Insert the circle's radius: "))
r = r/2
print(f"pi is {pi}\n"
      f"r is {r}")
print(f"The approximate area of this circle is {round(pi*(r**2),2)}")
