# 07 - Operações Aritméticas
"""
Operadores aritméticos:
+ Soma (5+2 == 7)
- Subtração (5-2 == 3)
/ Divisão (5/2 == 2.5)
* Multiplicação (5*2 == 10)
** Exponenciação (5**2 == 25)
// Divisão inteira (5//2 == 2)
% Resto (5%2 == 1)

Ordem de precedência:
1- ()
2- ** ou pow(base, expoente)
3- *, /, //, % (da esquerda para a direita)
4- +, - (da esquerda para a direita)
"""
print(5+3*8)  # == 29 (5+24)
print(3*5+4**2)  # == 31 (15+16)
print(3*(5+4)**2)  # == 243 (3*9**2 --> 3*81)
print(pow(9, 2))  # == 81 (9²)
print("Oi"*5)  # == "OiOiOiOiOi"
nome = input("Digite seu nome: ")
print(f"{nome:=<20}")  # Marcos==============
print(f"{nome:=^20}")  # =======Marcos=======
print(f"{nome:=>20}")  # ==============Marcos

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
print(f"A soma é: {n1 + n2}", end=' --> ')
print(f"O produto é: {n1 * n2}\n"
      f"A Divisão é: {n1 / n2}\n"
      f"A Divisão inteira é: {n1 // n2}")
# Para tirar a quebra: end='-->' (A soma é: 4 --> O produto é: 4)
# Para inserir quebra: \n





