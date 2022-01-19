# 06 - Tipos Primitivos e Saída de Dados

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1+n2
print("A soma entre {} e {} é {}".format(n1, n2, s))

# Aula 06B

n = int(input("Digite um valor: "))
print(n)
# vai imprimir 4
n = float(input("Digite um valor: "))
print(n)
# vai imprimir 4.0
n = str(input("Digite um valor: "))
print(n)
# vai imprimir 4 como uma string (não operacionalizável)
n = bool(input("Digite um valor: "))
print(n)
# vai imprimir "Verdadeiro" se for digitado qualquer valor,
# "Falso" se nada for digitado

n = input("Digite algo: ")
print(n.isnumeric())  # Verifica se é numérico
print(n.isdigit())  # Verifica se é dígito (exclui pontos, letras, inclui números sobre/subscritos (¹²³))
print(n.isdecimal())  # Verifica se é decimal (exclui pontos, letras, sobre/subscritos, considera apenas números)
print(n.isalnum())  # Verifica se é alfanumérico (letras e números)
print(n.isalpha())  # Verifica se é alfabético (letras apenas)
print(n.isascii())  # Verifica se é ASCII (padrão de caracteres em dispositivos eletrônicos (abc123!@#...)).
print(n.istitle())  # Verifica se as primeiras letras de cada palavra estão em maiúsculo
print(n.islower())  # Verifica se todas as letras estão em minúsculo
print(n.isupper())  # Verifica se todas as letras estão em maiúsculo
print(n.isspace())  # Verifica se uma string é composta apenas de espaço ('    ')
print(n.isidentifier())  # Verifica se é um identificador válido para uma variável: sem inicial maiúscula, por ex.)
