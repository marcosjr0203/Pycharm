"""
MÓDULO 2 - PYTHON BÁSICO
AULA 23
LISTAS
FATIAMENTO/APPEND/INSERT
POP/CLEAR/EXTEND/+/MIN/MAX
"""
# lista = ['jão', 'zé', 'juca', 'ciço']
# print(lista[2])
#
# lista = ['jão', 'zé', 'juca', 'ciço']
# print(lista[-2])
#
# lista = ['jão', 'zé', 'juca', 'ciço']
# lista[2] = 'mané'
# print(lista[2])
#
# lista = ['jão', 'zé', 'juca', 'ciço']
# print(lista[:3])
#
# lista = ['jão', 'zé', 'juca', 'ciço']
# print(lista[::2])
#
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista3 = (lista1 + lista2)
# print(lista3)
#
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista2.extend(lista1)
# print(lista2)
#
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista1.extend('A')
# print(lista1)
#
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista2.extend(7)
# print(lista2)
#
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista2.append(7)
# print(lista2)
#
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista2.insert(0, 3)
# print(lista2)
#
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista1.pop()
# print(lista1)

# lista = [1, 2, 3, 4, 5, 6, 7]
# del (lista[3])
# print(lista)

# lista = [1, 2, 3, 4, 5, 6, 7]
# print(max(lista))
# print(min(lista))

#lista = list(range(1, 10))
# print(lista)

# lista = 'Texto', True, 10, 5.75
# for elementos in lista:
#     print(f'{elementos} → {type(elementos)}')

secreto = 'perfume'
digitadas = []
while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Só pode digitar uma letra!')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print('Você acertou, digite outra letra')
    else:
        print('Você errou, digite outra letra')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Você acertou, {secreto_temporario}.')
        break
    else:
        print(f'{secreto_temporario}')
