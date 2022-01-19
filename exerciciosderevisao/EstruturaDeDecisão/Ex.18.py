"""
TODO 18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

TODO 19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
 unidades do mesmo.
 Observando os termos no plural a colocação do "e", da vírgula entre outros.
 Exemplo:
 326 = 3 centenas, 2 dezenas e 6 unidades
 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

TODO 20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada
 por aluno e apresentar:
 A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
 A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
 A mensagem "Aprovado com Distinção", se a média for igual a 10.

TODO 21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
 informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
 O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
 existentes na máquina.
 Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
 nota de 1;
 Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
 uma nota de 5 e quatro notas de 1.

TODO 22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo
 (resto da divisão).

TODO 23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
 Dica: utilize uma função de arredondamento.

TODO 24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
 O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
 par ou ímpar;
 positivo ou negativo;
 inteiro ou decimal.

TODO 25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
 "Telefonou para a vítima?"
 "Esteve no local do crime?"
 "Mora perto da vítima?"
 "Devia para a vítima?"
 "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
 Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
 e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

TODO 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
 Álcool:
 até 20 litros, desconto de 3% por litro
 acima de 20 litros, desconto de 5% por litro
 Gasolina:
 até 20 litros, desconto de 4% por litro
 acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de
 combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
 sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

TODO 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
 Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
 Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
 Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
 desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg)
 de maças adquiridas e escreva o valor a ser pago pelo cliente.

TODO 28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
 File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
 Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
 Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
 Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
 limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
 desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
 usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
 pagamento, valor do desconto e valor a pagar.
"""