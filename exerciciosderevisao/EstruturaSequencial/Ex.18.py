"""
TODO 19. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
import math as mat
fs = float(input("Enter the file size (in MB): "))
lv = float(input("Enter the link velocity (in Mbps): "))
vi = lv/8
min = fs/vi/60
print(f"The download of this file will take approximately {mat.ceil(min)} minutes")
