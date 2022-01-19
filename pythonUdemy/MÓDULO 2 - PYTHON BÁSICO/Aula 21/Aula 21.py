"""
MÓDULO 2 - PYTHON BÁSICO
AULA 21
ITERANDO STRINGS COM WHILE
"""
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

print('cnt\t\tstr')
while contador < tamanho_frase:
    # print(contador, '\t', '→', '\t', frase[contador])
    # nova_string += frase[contador]
    # print(nova_string)
    # contador += 1
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    contador += 1
print(nova_string)
