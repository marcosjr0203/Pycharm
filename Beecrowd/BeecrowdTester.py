# #1013
# A, B, C = input().split()
# A, B, C = int(A), int(B), int(C)
# MaiorAB = (A+B+abs(A-B))/2
# Maior = (MaiorAB+C+abs(MaiorAB-C))/2
# Maior = int(Maior)
# print(f"{Maior} eh o maior")
# print(type(Maior))

# #1014
# X = int(input())
# Y = float(input())
# C = X/Y
# C = float(C)
# print(f"{C:.3f} km/l")

# #1015
# import math
# x1, y1 = input().split()
# x2, y2 = input().split()
# x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
# distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
# print(f"{distance:.4f}")

# #1016
# distance = int(input())
# minutes = distance*2
# print(f"{minutes} minutos")

# #1017
# st = int(input())
# av = int(input())
# ln = av*st/12
# print(f"{ln:.3f}")

# #1018
# N = int(input())
# print(N)
# n100 = N // 100
# N -= n100*100
# n50 = N // 50
# N -= n50*50
# n20 = N // 20
# N -= n20*20
# n10 = N // 10
# N -= n10*10
# n5 = N // 5
# N -= n5*5
# n2 = N // 2
# N -= n2*2
# n1 = N // 1
# N -= n1
# print(n100, "nota(s) de R$ 100,00")
# print(n50, "nota(s) de R$ 50,00")
# print(n20, "nota(s) de R$ 20,00")
# print(n10, "nota(s) de R$ 10,00")
# print(n5, "nota(s) de R$ 5,00")
# print(n2, "nota(s) de R$ 2,00")
# print(n1, "nota(s) de R$ 1,00")

# #1019
# N = int(input())
# h = N//3600
# N -= h*3600
# m = N//60
# N -= m*60
# s = N
# print(f"{h}:{m}:{s}")

# #1020
# d = int(input())
# y = d//365
# d -= y*365
# m = d//30
# d -= m*30
# print(f"{y} ano(s)")
# print(f"{m} mes(es)")
# print(f"{d} dia(s)")

# #1021
# N = float(input())
# B = N//1
# C = float(N - B)
# B100 = int(B//100)
# B -= B100*100
# B50 = int(B//50)
# B -= B50*50
# B20 = int(B//20)
# B -= B20*20
# B10 = int(B//10)
# B -= B10*10
# B5 = int(B//5)
# B -= B5*5
# B2 = int(B//2)
# B -= B2*2
# C += B
# B = 0
# C100 = int(C//1)
# C -= C100*1
# C050 = int(C//0.5)
# C -= C050*0.5
# C025 = int(C//0.25)
# C -= C025*0.25
# C010 = int(C//0.1)
# C -= C010*0.1
# C005 = int(C//0.05)
# C -= C005*0.05
# C001 = round(C/0.01, 1)
# C -= C001*0.01
# print(f"NOTAS:")
# print(f"{B100} nota(s) de R$ 100.00")
# print(f"{B50} nota(s) de R$ 50.00")
# print(f"{B20} nota(s) de R$ 20.00")
# print(f"{B10} nota(s) de R$ 10.00")
# print(f"{B5} nota(s) de R$ 5.00")
# print(f"{B2} nota(s) de R$ 2.00")
# print(f"MOEDAS:")
# print(f"{C100} moeda(s) de R$ 1.00")
# print(f"{C050} moeda(s) de R$ 0.50")
# print(f"{C025} moeda(s) de R$ 0.25")
# print(f"{C010} moeda(s) de R$ 0.10")
# print(f"{C005} moeda(s) de R$ 0.05")
# print(f"{int(C001)} moeda(s) de R$ 0.01")

# # 1035
# """
#  Read 4 integer values A, B, C and D.
#  If B is greater than C and D is greater than A and if the sum of C
#  and D is greater than the sum of A and B and if C and D were positives
#  values and if A is even, write the message “Valores aceitos” (Accepted values).
#  Otherwise, write the message “Valores nao aceitos” (Values not accepted).
# """
#
# A, B, C, D = input().split(" ")
# A, B, C, D = int(A), int(B), int(C), int(D)
# if B > C and D > A:
#     if (C + D) > (A + B):
#         if C > 0 and D > 0:
#             if A % 2 == 0:
#                 print("Valores aceitos")
#             else:
#                 print("Valores nao aceitos")
#         else:
#             print("Valores nao aceitos")
#     else:
#         print("Valores nao aceitos")
# else:
#     print("Valores nao aceitos")
# """
# Read 3 floating-point numbers. After, print the roots of bhaskara’s formula.
# If it's impossible to calculate the roots because a division by zero or a square
# root of a negative number, presents the message “Impossivel calcular”."
# """
# import math
# A, B, C = input().split(" ")
# A, B, C = float(A), float(B), float(C)
# if A == 0:
#     print("Impossivel calcular")
# elif (B**2 - 4*A*C) < 0:
#     print("Impossivel calcular")
# else:
#     R1 = (- B + math.sqrt(B**2 - 4*A*C))/(2*A)
#     R2 = (- B - math.sqrt(B**2 - 4*A*C))/(2*A)
#     print(f"R1 = {R1:.5f}\n"
#           f"R2 = {R2:.5f}\n")

