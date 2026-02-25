from time import sleep
from os import system

quit = False
esc = ''

sessions = [[1, 0, 'Girls und Panzer - Das Finale'], [2, 0, 'Os Incríveis'], [3, 12, 'Os Sensacionais'], 
[4, 18, 'Red Dead'], [5, 16, 'Karython O Filme'], [6, 14, 'Git: O Hub']]

if len(sessions) > 0:
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
        
        system('cls')
        for i in range(len(sessions)):
            print(f'Sala {sessions[i][0]}: {sessions[i][2]}')
            print(f'Classificação indicativa: {sessions[i][1]} anos.''\n')
            sleep(0.2)
        
        try:
            esc = (int(input('Escola a sala com o filme que quer assistir: ')))
            system('cls')
        except ValueError:
            esc != ''
            print('Valor inválido para a sala. Reiniciando Programa.')
            sleep(1)
            continue
        
        if esc  < 1 or esc > len(sessions):
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
else:
    print('Não há nenhum filme para ver.')
    
     