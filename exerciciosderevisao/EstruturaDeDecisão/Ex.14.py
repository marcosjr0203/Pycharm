"""
TODO 14. Faça um programa que leia duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
 calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
 O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for
 A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""


def bulletin():
    g1 = float(input("Insert the first grade: "))
    g2 = float(input("Insert the second grade: "))
    while g1 > 10 or g2 > 10 or g1 < 0 or g2 < 0:
        print("Wrong data. Try again.")
        bulletin()
    name = " Final Average "
    concept = ""
    average = (g1 + g2) / 2
    result = ""
    if average < 4:
        concept = "E"
        result = "Failed"
    elif average < 6:
        concept = "D"
        result = "Failed"
    elif average < 7.5:
        concept = "C"
        result = "Passed"
    elif average < 9:
        concept = "B"
        result = "Passed"
    elif average < 10:
        concept = "A"
        result = "Passed"
    print(f"{name:=^50}\n1ST GRADE\t2ND GRADE\tAVERAGE\tCONCEPT\tRESULTS")
    print(f"\t{g1}\t\t\t{g2}\t\t  {average}\t\t{concept}\t{result}")


bulletin()
