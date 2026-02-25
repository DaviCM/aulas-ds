from time import sleep
from os import system


def start():
    try:
        if valid == True:
            print('\n'f'{8 * '-'} Bem vindo ao CINEMÁTICO! {8 * '-'}')
            watch()
    except:
        print('Não há nenhum filme para ver. O operador deve adicionar filmes.')

    else:
        print('Não há nenhum filme para ver.')


def get_movie():
    num_movies = int(input('\n''Digite a quantidade de filmes desejada: '))
    sessions = []
    
    if num_movies != 0:
        for i in range(num_movies):
            print('\n'f'{8 * '-'} Adicione o {i + 1}° filme: {8 * '-'}''\n')
            
            room = int(input('Insira a sala em que o filme está: ').strip())
            idade_filme = int(input('Insira a classificação indicativa: ').strip())
            nome_filme = input('Insira o nome do filme: ').capitalize()
            
            sessions.append([room, idade_filme, nome_filme])

            print('\n'f'{8 * '-'} Filme {i + 1} adicionado! {8 * '-'}')
            sleep(0.2)
            system('cls')
            
        print(sessions)
        return True, sessions
    else:
        return False, None


def get_user():
    nome = input('Insira seu nome: ').capitalize()
            
    try:
        id_cliente = int(input('Insira sua idade: '))
    except ValueError:
        print('Valor inválido para a idade. Tente novamente.')
        return False, None, None
        
    print(f'Obrigado por se cadastrar, {nome}!')
    return True, nome, id_cliente


def watch():
    valid, nome, id_cliente = get_user()
    while True:
        if valid == True:
            system('cls')
            for i in range(len(sessions)):
                print(f'Sala {sessions[i][0]}: {sessions[i][2]}')
                print(f'Classificação indicativa: {sessions[i][1]} anos.''\n')
                sleep(0.2)
            
            try:
                esc = (int(input('Escolha a sala com o filme que quer assistir: ')))
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
                break
        else:
            print('Por favor, insira dados válidos.')


while True:
    print(f'{8 * '-'} Menu de operações do cinema {8 * '-'}')
    print('\n''1 - Cliente')
    sleep(0.2)
    print('2 - Operador')
    permission = input('\n''Digite a operação que deseja realizar: ')

    try:
        sleep(1)
        system('cls')

        if permission < 1 or permission > 2:
            print('Por favor, insira um valor válido.')
            sleep(1)
            system('cls')
            continue

        elif permission == 1:
            start()

        else:
            valid, sessions = get_movie()

    except ValueError:
        print('Essa operação não existe. Reiniciando sistema.')
        continue



