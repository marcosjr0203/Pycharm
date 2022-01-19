"""
MÓDULO 3
AULA 10
SISTEMA DE PERGUNTAS E RESPOSTAS COM DICIONÁRIOS
"""
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5', },
        'resposta_certa': '4',
        'resposta_certa2': 'b',
    }, 'Pergunta 2': {
        'pergunta': 'Quanto é 2+3?',
        'respostas': {'a': '1', 'b': '4', 'c': '5', },
        'resposta_certa': '5',
        'resposta_certa2': 'c',
    }, 'Pergunta 3': {
        'pergunta': 'Quanto é 2-1?',
        'respostas': {'a': '1', 'b': '4', 'c': '5', },
        'resposta_certa': '1',
        'resposta_certa2': 'a',
    }, 'Pergunta 4': {
        'pergunta': 'Quanto é 1+4?',
        'respostas': {'a': '1', 'b': '4', 'c': '5', },
        'resposta_certa': '5',
        'resposta_certa2': 'c',
    }, 'Pergunta 5': {
        'pergunta': 'Quanto é 5-1?',
        'respostas': {'a': '1', 'b': '4', 'c': '5', },
        'resposta_certa': '4',
        'resposta_certa2': 'b',
    },
}
pontos = 0

for chperg, valper in perguntas.items():
    print(f'{chperg}: {valper["pergunta"]}')
    print('Escolha uma das opções:')
    for chresp, valresp in valper['respostas'].items():
        print(f'[{chresp}]: {valresp}')

    resposta = input('Sua resposta: ').lower()
    if resposta == valper['resposta_certa'] or \
            resposta == valper['resposta_certa2']:
        print('Parabéns! Resposta Correta!')
        pontos += 1
    else:
        print('Resposta Incorreta!')
print(f'Você acertou {pontos} de 5 questões.')
if pontos == 5:
    print('Excelente!!')
if pontos == 4:
    print('Muito bom!')
if pontos == 3:
    print('Razoável.')
if pontos == 2:
    print('Está ruim.')
if pontos == 1:
    print('Muito ruim!')
if pontos == 0:
    print('Péssimo!!')
