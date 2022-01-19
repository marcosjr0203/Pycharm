"""
MÓDULO 2 - PYTHON BÁSICO
AULA 33
GERADOR DE CPF
"""
from random import randint
numero = str(randint(100000000, 999999999))

novo_cpf = numero                   # 9 números aleatórios
reverso = 10                        # Contador reverso
total = 0                           # O total das multiplicações

# Loop do CPF
for index in range(19):
    if index > 8:                   # Primeiro índice vai de 0 a 9,
        index -= 9                  # São os 9 primeiros digitos do CPF

    total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

    reverso -= 1                    # Decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:                   # Se o digito for > que 9 o valor é 0
            d = 0
        total = 0                   # Zera o total
        novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

print(novo_cpf)
