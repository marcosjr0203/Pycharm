"""
TODO 12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
 que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
 Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
 descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
 Desconto do IR:
 Salário Bruto até 900 (inclusive) - isento
 Salário Bruto até 1500 (inclusive) - desconto de 5%
 Salário Bruto até 2500 (inclusive) - desconto de 10%
 Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
 abaixo.
 No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""
h = float(input("Enter the salary per hour: $"))
d = float(input("Enter the hours worked in the month: "))
a = h*d
s = a*0.03
f = a*0.11
i = [0, 0.05, 0.1, 0.2]
if a <= 900:
    i = i[0]
    p = "0%"
elif a <= 1500:
    i = a*i[1]
    p = "5%"
elif a <= 2500:
    i = a*i[2]
    p = "10%"
else:
    i = a * i[3]
    p = "20%"
title = "HOLLERIT"
print(f"h={h}\nd={d}\na={a}\ns={s}\nf={f}\ni={i}")
print(f"{title:=^40}\n"
      f"- Sindicate:\t\t${s:.2f}\n"
      f"- Inc. Tax ({p}):\t${i:.2f}\n"
      f"* Warr. Fund:\t\t${f:.2f}\n"
      f"{'':_^40}\n"
      f"GROSS SALARY:\t\t${a:.2f}\n"
      f"TOTAL DISCOUNTS:\t${(s+i):.2f}\n"
      f"LIQUID SALARY:\t\t${a-(s+i):.2f}")





