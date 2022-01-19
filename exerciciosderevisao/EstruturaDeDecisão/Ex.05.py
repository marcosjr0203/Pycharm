"""
TODO 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada
 por aluno e apresentar:
 A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
 A mensagem "Reprovado", se a média for menor do que sete;
 A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
g1 = float(input("Enter the 1st grade: "))
g2 = float(input("Enter the 2nd grade: "))
av = (g1+g2)/2
if av <= 9:
    print(f"Average: {av}. Approved.")
elif av < 7:
    print(f"Average: {av}. Failed.")
elif av == 10:
    print(f"Average: {av}. Approved with distinction.")
else:
    print("Wrong values for grades (0-10). Try again.")
