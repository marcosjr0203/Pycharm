"""
TODO 16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
 pedir os  valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
 Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
 demais valores, sendo encerrado;
 Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
 Se o delta calculado for igual a zero, a equação possui apenas uma raiz real; informe-a ao usuário;
 Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
import math


def rootscalc():
    title = "ROOTS CALCULATOR"
    print(f"{title:²^40}")
    a = float(input("Enter the 'a' term (ax²): "))
    if a == 0:
        ans = input("It's not a second degree equation (a = 0).\nTry again (y/n)?")
        if ans.lower() == 'y':
            rootscalc()
        else:
            print("Bye.")
            exit()
    else:
        b = float(input("Enter the 'b' term (bx): "))
        c = float(input("Enter the 'c' term: "))
        delta = (b**2) - (4*a*c)
        if delta == 0:
            print("This equation has only one real root.")
        elif delta > 0:
            print("This equation has two real roots.")
        elif delta < 0:
            ans = input(f"This equation has no real roots (Delta = {delta}).\nTry again (y/n)?")
            if ans.lower() == 'y':
                rootscalc()
            else:
                print("Bye.")
                exit()
        sqd = math.sqrt(delta)
        print(sqd)
        xl = (-b + sqd) / 2 * a
        xll = (-b - sqd) / 2 * a
        print(f"Delta value: {delta}")
        print(f"Roots of this equation: {xl:.2f}, {xll:.2f}")
        ans = input("Try again (y/n)?")
        if ans.lower() == 'y':
            rootscalc()
        else:
            print("Bye.")
            exit()


rootscalc()




