"""
TODO 11. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
 salário atual:
 salários até R$ 280,00 (incluindo) : aumento de 20%
 salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
 salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
 salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
 o salário antes do reajuste;
 o percentual de aumento aplicado;
 o valor do aumento;
 o novo salário, após o aumento.
"""
s = float(input("Type your current salary: "))
if s <= 280:
    print(f"Your current salary is {s:.2f}.\n"
          f"Your salary will be increased by 20% corresponding to ${s*0.2}.\n"
          f"Your new salary will be ${(s*1.2):.2f}")
elif s <= 700:
    print(f"Your current salary is {s:.2f}.\n"
          f"Your salary will be increased by 15% corresponding to ${s*0.15}.\n"
          f"Your new salary will be ${(s*1.15):.2f}")
elif s <= 1500:
    print(f"Your current salary is {s:.2f}.\n"
          f"Your salary will be increased by 10% corresponding to ${s*0.10}.\n"
          f"Your new salary will be ${(s*1.10):.2f}")
else:
    print(f"Your current salary is {s:.2f}.\n"
          f"Your salary will be increased by 5% corresponding to ${s * 0.05}.\n"
          f"Your new salary will be ${(s * 1.05):.2f}")
