"""
TODO 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
15.1. salário bruto.
15.2. quanto pagou ao INSS.
15.3. quanto pagou ao sindicato.
15.4. o salário líquido.
15.5. calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
s = float(input("Type your salary per hour: "))
h = int(input("Type your hours worked in this month: "))
gs = s*h
r = gs*0.11
iss = gs*0.08
sind = gs*0.05
print("HOLLERIT:\n"
      f"+ Gross Salary: US$ {gs:.2f}\n"
      f"- Rent Tax: US$ {r:.2f}\n"
      f"- ISS: US$ {iss:.2f}\n"
      f"- Sindicate: US$ {sind:.2f}\n"
      f"= Total discounted: US$ {(r+iss+sind):.2f}\n"
      f"= Liquid Salary: US$ {(gs-r-iss-sind):.2f}")