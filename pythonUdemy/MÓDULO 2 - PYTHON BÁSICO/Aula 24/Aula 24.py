"""
MÓDULO 2 - PYTHON BÁSICO
AULA 24
FOR...ELSE
"""
variavel = ['Marcos', 'Samira', 'Neto', 'Michel', 'Marvin']
comeca_com_m = False
for valor in variavel:
    if valor.startswith('M'):
        comeca_com_m = True
if comeca_com_m:
    print('Existem nomes que começam com "M" nessa Lista.')
else:
    print('Nâo existe nenhuma palavra que começa com "M".')