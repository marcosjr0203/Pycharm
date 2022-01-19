# Desafio 005 - Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor
n1 = int(input("Digite um número inteiro: "))
print(f"Número digitado: {n1}\nAntecessor de {n1}: {n1-1}\nSucessor de {n1}: {n1+1}")
# Desafio 006 - Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz
n2 = int(input("Digite um número inteiro: "))
print(f"Número digitado: {n2}\nDobro de {n2}: {n2*2}\nTriplo de {n2}: {n2*3}\nRaiz de {n2}: {n2**(1/2):.2f}")
# Desafio 007 - Desenvolva um programa que leia duas notas de um aluno e calcule sua média
n3 = int(input("Digite a primeira nota: "))
n4 = int(input("Digite a segunda nota: "))
print(f"A média do aluno foi {(n3+n4)/2}")
# Desafio 008 - Escreva um programa que leia um valor em metros e o converta em cm e mm
n5 = float(input("Digite um valor, em metros: "))
print(f"Valor digitado: {n5} metros.\nValor em centímetros: {n5*100}\nValor em milímetros: {n5*1000}")
# Desafio 009 - Faça um programa que leia um número inteiro e imprima sua tabuada
n6 = int(input("Digite um número inteiro: "))
print(f"Tabuada do {n6}: ")
for n in range(1, 11):
    print(f"{n6} x {n} = {n6*n}")
# Desafio 010 - Crie um algoritmo que converta real em dólar (considere R$ 1,00 == US$ 5,44 (01/05/21))
n7 = float(input("Digite o valor em R$: "))
print(f"Valor em dólar: US$ {n7/5.44:.2f}")
# Desafio 011 - Desenvolva um programa que leia a largura e a altura de uma parede, em metros, calcule
# a sua área, e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma
# área equivalente a 2m².
n8 = float(input("Digite a largura: "))
n9 = float(input("Digite a altura: "))
print(f"Quantidade necessária de tinta: {n8*n9/2:.2f} litros.")
# Desafio 012 - Escreva um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
n10 = float(input("Digite o preço: "))
print(f"Valor do produto com 5% de desconto: R$ {n10*0.95:.2f}")
# Desafio 012 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
n11 = float(input("Digite o salário: "))
print(f"Novo salário, com 15% de aumento: {n11*1.15:.2f}")