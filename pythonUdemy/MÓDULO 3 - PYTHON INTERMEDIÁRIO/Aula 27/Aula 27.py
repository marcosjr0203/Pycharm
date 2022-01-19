"""
MÓDULO 3
AULA 27
TRY...EXCEPT
"""
# try:
#     print(a)
# except:
#     print('Erro')

# try:
#     print(a)
# except NameError as erro:
#     print('Erro:', erro)

try:
    print(a)
except NameError as error:
    print('Erro 1:', error)

try:
    a = []
    print(a[1])
except IndexError as error:
    print('Erro 2:', error)

try:
    a = {}
    print(a[1])
except KeyError as error:
    print('Erro 3:', error)

try:
    print(a*9)
except Exception as error:
    print('Erro 4:', error)

else:
    print('Continue')

finally:
    print('Reinicializando o programa')

