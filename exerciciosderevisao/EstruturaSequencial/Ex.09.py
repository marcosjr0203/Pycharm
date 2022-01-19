"""
TODO 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
fd = float(input("Insert degrees, in Fahrenheit: "))
print(f"{fd}ºF correspond to {(5*(fd-32)/9):.2f}ºC")
