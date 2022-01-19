"""
MÓDULO 4
AULA 6
ENCAPSULAMENTO
public, protected, private
"""

#DADOS PÚBLICOS
# class BaseDeDados:
#     def __init__(self):
#         self.dados = {}
#
#     def inserir_cliente(self, id, nome):
#         if 'clientes' not in self.dados:
#             self.dados['clientes'] = {id: nome}
#         else:
#             self.dados['clientes'].update({id: nome})
#
#     def lista_clientes(self):
#         for id, nome in self.dados['clientes'].items():
#             print(id, nome)
#
#     def apaga_cliente(self,id):
#         del self.dados['clientes'][id]
#
# bd = BaseDeDados()
# bd.inserir_cliente(1, 'Marcos')
# bd.inserir_cliente(2, 'Samira')
# bd.inserir_cliente(3, 'Marvin')
# bd.inserir_cliente(4, 'Marcos Neto')
# bd.inserir_cliente(5, 'Michel')
# print(bd.dados)
# bd.apaga_cliente(3)
# bd.lista_clientes()
# bd.dados = 'outracoisa'
# bd.lista_clientes()



# # DADOS PROTEGIDOS
# class BaseDeDados:
#     def __init__(self):
#         self._dados = {}
#
#     def inserir_cliente(self, id, nome):
#         if 'clientes' not in self._dados:
#             self._dados['clientes'] = {id: nome}
#         else:
#             self._dados['clientes'].update({id: nome})
#
#     def lista_clientes(self):
#         for id, nome in self._dados['clientes'].items():
#             print(id, nome)
#
#     def apaga_cliente(self,id):
#         del self._dados['clientes'][id]
#
# bd = BaseDeDados()
# bd.inserir_cliente(1, 'Marcos')
# bd.inserir_cliente(2, 'Samira')
# bd._dados = 'outracoisa'
# bd.lista_clientes()


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self,id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Marcos')
bd.inserir_cliente(2, 'Samira')
bd.__dados = 'outracoisa'
print(bd.__dados)

