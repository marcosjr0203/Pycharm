"""
MÓDULO 2 - PYTHON BÁSICO
AULA 5
FORMATANDO VALORES COM MODIFICADORES
:s - STRINGS
:d - INTEGERS
:f - FLOATS
:. (N.º)f -QUANTIDADE DE CASAS DECIMAIS (FLOAT)
:(CARACTERE) (> OU < OU ^) (QUANTIDADE)(TIPO - s, d OU f)
> - ESQUERDA
< - DIREITA
^ - CENTRO
"""
# FORMATAÇÃO DE FLOATS - :f
n1 = 10
n2 = 3
div = 10/3
print('{:.2f}'.format(div))
print(f'{div:.2f}')

# FORMATAÇÃO DE STRINGS - :s
nome = 'Marcos'
print('{:.3s}'.format(nome))
print(f'{nome :.3s}')
print(f'{nome:*>10}')
print(f'{nome:-<10}')
print(f'{nome:~^10}')

# FORMATAÇÃO DE INTEGERS - :d
valor = 1111
print(f'{valor:0>10}')
print(f'{valor:0<10}')
print(f'{valor:0^10}')

# LJUST E RJUST
nome = 'Marcos'
nome_format1 = nome.ljust(10, "+")
nome_format2 = nome.rjust(10, "-")
print(nome_format1)
print(nome_format2)

# UPPER, LOWER E TITTLE
nome = 'mArCoS'
print(nome.upper())
print(nome.lower())
print(nome.title())