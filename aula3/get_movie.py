def get_movie():
    from time import sleep
    from os import system
    
    num_movies = int(input("Digite a quantidade de filmes desejada: "))
    sessions = []
    
    if num_movies != 0:
        for i in range(num_movies):
            print('\n'f'{8 * '-'} Adicione o {i + 1}° filme: {8 * '-'}''\n')
            
            room = int(input('Insira a sala em que o filme está: ').strip())
            idade_filme = int(input('Insira a classificação indicativa: ').strip())
            nome_filme = input('Insira o nome do filme: ')
            
            sessions.append([room, idade_filme, nome_filme])

            print('\n'f'{8 * '-'} Filme {i + 1} adicionado! {8 * '-'}')
            sleep(0.2)
            system('cls')
            
        print(sessions)
        return True, sessions
    else:
        return False, None
    
    