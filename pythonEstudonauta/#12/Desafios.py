# Desafio 36 - Escreva um programa para aprovar um empréstimo bancário.
# O programa precisa perguntar o valor do empréstimo, o salário do cliente e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário do cliente.
# valor = input("Qual o valor do empréstimo?\n")
# sal = input("Qual seu salário?\n")
# anos = input("Em quantos anos deseja pagar?\n")
# anos = int(anos)
# meses = int(anos*12)
# valor = int(valor)
# sal = int(sal)
# parcela = valor/meses
# if parcela >= sal*30/100:
#     print(f"Empréstimo não liberado. Valor da parcela excede 30%: RS {parcela},00")
# else:
#     print(f"Empréstimo liberado. Valor da parcela: RS {parcela:.2f}")

# Desafio 37 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão: 1-binário/2-octal/3-hexadecimal.
# Decimal para binário
dec = input("Digite um valor decimal: ")
binlist = []
term = dec
for item in dec:
    item = int(item)
    while int(term) >= 1:
        if item % 2 == 0:
            binlist += term






# Desafio 38 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O 1º valor é maior;
# - O 2º valor é maior;
# - Ambos são iguais.

# Desafio 39 - Escreva um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar no serviço militar;
# - Se ele já é tempo de se alistar;
# - Se ele já passou do tempo de se alistar.
# O programa também deverá mostrar o tempo que falta ou que passou do alistamento.
# Desafio 40 - Escreva um programa que leia duas notas de um aluno e calcule sua média mostrando uma mensagem no final:
# - abaixo de 5.0: reprovado
# - entre 5.0 e 6.9: em recuperação
# - acima de 7.0: aprovado

# Desafio 41 - Escreva um programa que leia o ano de nascimento de um atleta e mostre sua categoria, conforme a idade:
# - até 9 anos: mirim
# - até 14 anos: infantil
# - até 19 anos: júnior
# - até 20 anos: sênior
# - acima de 20: master

# Desafio 42 - Refaça o desafio 35 acrescentando a informação do tipo de triângulo (equilátero, isosceles, escaleno).

# Desafio 43 - Escreva um programa que calcule o IMC e informe seu status de acordo com ele:
# - Abaixo de 18.5: Abaixo do peso;
# - Entre 18.5 e 25: Peso ideal;
# - Entre 25 e 30: sobrepeso;
# - Entre 30 e 40: Obeso;
# - Acima de 40: Obesidade mórbida.

# Desafio 44 - Escreva um programa que calcule o valor a ser pago por um produto, considerando seu preço normal
# e condição de pagamento:
# - à vista no dinheiro ou cheque: 10% de desconto;
# - à vista no cartão de crédito: 5% de desconto;
# - em até 2x no cartão de crédito: preço normal;
# - acima de 3x no cartão de crédito: 20% de juros.

# Desafio 45 - Escreva um programa de jokenpô