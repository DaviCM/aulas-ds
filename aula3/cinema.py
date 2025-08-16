from time import sleep
from os import system

sessions = [[1, 0, 'Girls und Panzer - Das Finale'], [2, 10, 'Herobrine - A Lenda'], [3, 12, 'Guerra nas IDEs - O Retorno de Java'],
            [4, 14, 'Carro Pika vs Celta 2012'], [5, 16, 'Velozes e Furiosos - Desafio em Ceilândia'], [6, 18, 'Red Dead Redemption']]

quit = False
esc = ''

while quit == False:
    print('\n'f'{8 * '-'} Bem vindo ao CINEMÁTICO! {8 * '-'}')
    if esc == '':
        nome = input('Insira seu nome: ').capitalize()
        
        try:
            id_cliente = int(input('Insira sua idade: '))
        except ValueError:
            print('Valor inválido para a idade. Reiniciando programa.')
            continue
        
    else:
        pass
    
    for i in range(6):
        print(f'Sala {sessions[i][0]}: {sessions[i][2]}')
        print(f'Classificação indicativa: {sessions[i][1]} anos.''\n')
        sleep(0.2)
 
    esc = (int(input('Escola a sala com o filme que quer assistir: ')))
    system('cls')
    
    if esc  < 1 or esc > 6:
        print('Valor inválido. Reiniciando programa.')
        continue

    if id_cliente < sessions[esc - 1][1]:
        print('Você não pode assistir ao filme. Escolha um com a classificação adequada.')
        sleep(1)
        continue
        
    else:
        print('\n'f'{8 * '-'} Dados da sessão: {8 * '-'} ')
        print(f'Nome: {nome}')
        print(f'Sala: {sessions[esc - 1][0]}')
        print(f'Filme: {sessions[esc - 1][2]}''\n')
        print(f'Bom filme!')
        quit = True
    
        