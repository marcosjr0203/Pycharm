"""
MÓDULO 2 - PYTHON BÁSICO
AULA 31
DESAFIO VALIDE UM CPF
CPF = 168.995.350-09
----------------------------------------------
1 * 10 = 10             #   1 * 11 = 11
6 * 9 = 54              #   6 * 10 = 60
8 * 8 = 64              #   8 * 9 = 72
9 * 7 = 63              #   9 * 8 = 72
9 * 6 = 54              #   9 * 7 = 63
5 * 5 = 25              #   5 * 6 = 30
3 * 4 = 12              #   3 * 5 = 15
5 * 3 = 15              #   5 * 4 = 20
0 * 2 = 0               #   0 * 3 = 0
                        #D1→0 * 2 = 0
SOMA = 297              #   SOMA =
10º DÍGITO =            #   11ºDÍGITO =
11 - (297 % 11) = 11    #   11 - (343 % 11) = 9
SE 11 > 9 = 0           #   DÍGITO 2 = 9
DIGITO 1 = 0            #
---------------------------------------------------
"""
cpf = input(f'CPF: ')
# 1 - VALIDAÇÃO DO CPF:
if cpf.isnumeric():
    print(cpf[:3], '.', cpf[3:6], '.', cpf[6:9], '-', cpf[9:])
else:
    print('Digite somente números')
if len(cpf) != 11:
   print('ERRO! Você deve digitar 11 algarismos.')
# 2 - CÁLCULO DO DÉCIMO DÍGITO
dig1 = list(cpf[:9])
mult1 = list(range(10, 1, -1))
d1, d2, d3, d4, d5, d6, d7, d8, d9 = dig1
m1, m2, m3, m4, m5, m6, m7, m8, m9 = mult1
opr1 = ((int(d1) * int(m1))
        + (int(d2) * int(m2))
        + (int(d3) * int(m3))
        + (int(d4) * int(m4))
        + (int(d5) * int(m5))
        + (int(d6) * int(m6))
        + (int(d7) * int(m7))
        + (int(d8) * int(m8))
        + (int(d9) * int(m9)))
# print(opr1)
dcm = 11 - (opr1 % 11)
if dcm > 9:
    dcm = 0
else:
    dcm = dcm
# print(dcm)
# CÁLCULO DO DÉCIMO PRIMEIRO DÍGITO
dig2 = list(cpf[:10])
mult2 = list(range(11, 1, -1))
d21, d22, d23, d24, d25, d26, d27, d28, d29, dcm = dig2
m21, m22, m23, m24, m25, m26, m27, m28, m29, m210 = mult2
opr2 = ((int(d21) * int(m21))
        + (int(d22) * int(m22))
        + (int(d23) * int(m23))
        + (int(d24) * int(m24))
        + (int(d25) * int(m25))
        + (int(d26) * int(m26))
        + (int(d27) * int(m27))
        + (int(d28) * int(m28))
        + (int(d29) * int(m29))
        + (int(dcm) * int(m210)))
# print(opr2)
dcp = 11 - (opr2 % 11)
if dcp > 9:
    dcp = 0
else:
    dcp = dcp
# print(dcp)
if int(cpf[-1]) == int(dcp) and int(cpf[-2]) == int(dcm):
    print('CPF validado')
else:
    print('CPF não validado')
