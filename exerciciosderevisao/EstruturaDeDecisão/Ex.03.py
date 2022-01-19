"""
TODO 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
 Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
g = input("Enter your gender: ")
if g.upper() == "F":
    print("Gender: Female")
elif g.upper() == "M":
    print("Gender: Male")
else:
    print("Invalid Gender")
