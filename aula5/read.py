from os import system, name
from time import sleep

while True:
    try:
        filename = (input('Digite o nome do arquivo, sem extensão: ').lower()).strip()

        # Nome do arquivo que será aberto, parÂmetro de modo 'r' para identificar que a operação é leitura do arquivo e 'encoding=utf-8' identifica o formato de codificação.
        with open(f'{filename}.txt', 'r', encoding='utf-8') as file:
            open_file = file.read()

        system('cls' if name == 'nt' else 'clear')

        print(open_file)

        quit = (input('\n''Deseja abrir outro arquivo? (s/n): ').lower()).strip()
        if quit == 's':
            system('cls')
            continue
        else:
            print('\n''Adeus.')
            break

    # Exception geralmente é usada com o alias 'e', mas não é obrigatório (para não confundir com as classes)
    except Exception as e:
        print(f'Não foi possível ler o arquivo. Erro: {e}' )
        sleep(1)
        system('cls')
        continue

