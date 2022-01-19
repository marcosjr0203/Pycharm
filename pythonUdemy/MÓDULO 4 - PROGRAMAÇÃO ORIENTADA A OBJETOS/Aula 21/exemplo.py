# FORMA SIMPLES (PRECISA DO 'CLOSE')
arquivo = open('abc.txt', 'w')
arquivo.write('Texto')
arquivo.close()

# GERENCIADOR DE CONTEXTO (DISPENSA 'CLOSE')
with open('abc.txt', 'w') as arquivo:
    arquivo.write('Texto')

# CLASSE COMO GERENCIADOR DE CONTEXTO
class Arquivo:
    def __init__(self, arquivo, modo):
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.arquivo.close()

with open('abc.txt', 'w') as arquivo:
    arquivo.write('Texto')