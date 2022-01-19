"""
MÓDULO 2 - PYTHON BÁSICO
AULA 10
CONDIÇÕES IF, ELIF e ELSE + Booleans
"""
nome = input("Qual seu nome? ")
ano_nasc = int(input("Em que ano você nasceu? "))
print('Se você nasceu em ', ano_nasc, 'então você já tem ', 2021-ano_nasc)
if 2021 - ano_nasc < 12:
    print('Você é uma criança, gugudadá!')
elif 2021 - ano_nasc < 18:
    print('Você ainda é um adolescente, bicho.')
elif 2021 - ano_nasc < 50:
    print('Caramba, mano, você já é adulto!')
elif 2021 - ano_nasc < 80:
    print('Eita, você é velho!')
else:
    print('Putz, tu é um ancião')