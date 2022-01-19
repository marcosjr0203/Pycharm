"""
MÓDULO 3
AULA 29
USO DE TRY E EXCEPT COMO CONDICIONAL
"""
def conversao(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    numero = conversao(input('Digite um número: '))
    if numero is not None:
        print(numero/2)
    else:
        print('Erro! digite um valor numérico')
