"""
MÓDUL0 4
AULA 1
CLASSES - PYTHON ORIENTADO A OBJETOS (POO)
"""
from Pessoa import Pessoa

# # DEFININDO UMA INSTÂNCIA E UTILIZANDO UM MÉTODO
# p1 = Pessoa()
# p2 = Pessoa()
#
# p1.falar()

# ENVIANDO DADOS AO OBJETO 'PADRÃO' CRIADO (CLASS)
p1 = Pessoa('Marcos', 37)
p2 = Pessoa('Samira', 38)
p1.comer('arroz')
p2.comer('amendoim')
p1.falar('astronomia')
p1.parar_comer()
p1.falar('matemática')
p1.falar('programação de computadores')
print(p1.ano_nasc())
print(p2.ano_nasc())