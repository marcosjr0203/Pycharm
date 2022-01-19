"""
TODO 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e
mostre  o total do seu salário no referido mês.
"""
sph = float(input("Enter your salary per hour: "))
whim = int(input("Ok. Now, enter the amount of your hours worked, in the period of one month: "))
print(f"Your monthly salary is US$ {float(sph*whim):.2f}")
