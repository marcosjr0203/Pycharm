frase = "Curso em Vídeo Python"
print(frase[9])
print(frase[:8])
print(frase[9:])
print(frase[::2])
print(frase[9::2])
print(len(frase))
print(frase.count("o"))
print(frase.count("o"))
print(frase.count("o", 0, 13))
print(frase.find("deo"))
print(frase.replace("Python", "Android"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase2 = "   Aprenda Python  "
print(frase2.strip()) # remove espaços inúteis no início e no final da frase
print(frase2.rstrip()) # remove espaços inúteis no início da frase
print(frase2.lstrip()) # remove espaços inúteis no final da frase
print(frase.split()) # divide a frase em partes, usando espaço como separador
print(" ".join(frase)) # junta as palavras, usando espaço como separador
