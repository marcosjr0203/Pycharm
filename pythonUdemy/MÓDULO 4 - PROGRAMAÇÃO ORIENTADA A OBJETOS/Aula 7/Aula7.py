"""
MÓDULO 4
AULA 7
RELAÇÃO ENTRE CLASSES
ASSOCIAÇÃO
"""
from Classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('João')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever('Olivetti')

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
