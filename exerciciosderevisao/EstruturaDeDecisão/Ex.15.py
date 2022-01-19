"""
TODO 15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
 triângulo.
 Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
 Dicas:
 Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos
 outros dois e maior que o valor absoluto da diferença entre essas medidas.
 Triângulo Equilátero: três lados iguais;
 Triângulo Isósceles: quaisquer dois lados iguais;
 Triângulo Escaleno: três lados diferentes;
"""
name = " Is it a Triangle?? "
print(f"{name:*^50}")
s1 = float(input(f"Enter the 1st side: "))
s2 = float(input(f"Enter the 2nd side: "))
s3 = float(input(f"Enter the 3rd side: "))


def istriangle():
    if (s1 + s2) > s3 and (abs(s1 - s2) < s3) or\
            (s1 + s3) > s2 and (abs(s1 - s3) < s2) or\
            (s3 + s2) > s1 and (abs(s3 - s2) < s1):
        if s1 == s2 == s3:
            print("It's an equilateral triangle.")
        elif s1 == s2 != s3 or s1 == s3 != s2 or s3 == s2 != s1:
            print("It's an Isosceles triangle.")
        else:
            print("It's a Scalen triangle.")
    else:
        print("Unable to create triangle with given sides/angles.\n"
              "Side lengths do not adhere to the triangle inequality theorem, "
              "which states that the sum of the side lengths of any 2 sides "
              "of a triangle must exceed the length of the third side.")


istriangle()
