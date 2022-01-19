# #1021
# import math
# N = float(input())
# B = N//1
# C = float(N-B)
# bval = [100, 50, 20, 10, 5, 2]
# cval = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
# bills = []
# coins = []
# bcounter = 0
# ccounter = 0
# while bcounter < len(bval):
#     for item in bval:
#         bills.append(int(B//bval[bcounter]))
#         B -= bills[bcounter]*bval[bcounter]
#         bcounter += 1
# C += B
# print(C)
# while ccounter < len(cval):
#     for item in cval:
#         coins.append(C//cval[ccounter])
#         C -= coins[ccounter]*cval[ccounter]
#         ccounter += 1
# b = 0
# c = 0
# print("NOTAS:")
# while b < len(bills):
#     print(f"{int(bills[b])} nota(s) de R$ {bval[b]:.2f}")
#     b += 1
# print("MOEDAS:")
# while c < len(coins):
#     print(f"{int(coins[c])} moeda(s) de R$ {cval[c]:.2f}")
#     c += 1
# print(C)

mensagem = input("Escreva sua mensagem: ")
print(mensagem)