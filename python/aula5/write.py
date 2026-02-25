from os import system, name
from time import sleep

while True:
    try:
        filename = input('Digite o nome do arquivo (sem extensão): ').lower()
        system('clear' if name == 'posix' else 'cls')

        print('Escolha a opção que deseja realizar:''\n')
        print('1 - Ver texto do arquivo')
        print('2 - Sobrescrever texto do arquivo')
        print('3 - Adicionar texto ao arquivo')
        print('4 - Ir embora')

        choice = (input('Escolha o que deseja fazer: ').lower()).strip()

        if choice == '1':
            system('cls')

            with open(f'{filename}.txt', 'r', encoding='utf-8') as file:
                # Único argumento do read é o tamanho, não se deve passar o arquivo.
                openfile = file.read()

                print(openfile)
        
        elif choice == '2':
            system('cls')
            newtext = input('Digite o que deseja escrever no arquivo: ')

            # Parâmetro de modo se tornou 'w' pois agora realizaremos escrita no arquivo.
            with open(f'{filename}.txt', 'w', encoding='utf-8') as file:
                file.write(newtext)

            print('O texto foi inserido no arquivo!')

        elif choice == '3':
            system('cls')          
            newtext = input('Digite o que deseja escrever no arquivo: ')
            # Parâmetro de modo se tornou 'a' de append, na função de adicionar escrita sem sobrescrever.
            with open(f'{filename}.txt', 'a', encoding='utf-8') as file:
                file.write('\n')
                file.write(newtext)

            print('O texto foi adicionado ao arquivo!')

        elif choice == '4':
            system('cls')
            print('\n''Já vai tarde.')
            break

        else:
            system('cls')
            print('Opção inválida. Reiniciando.')
            sleep(1)
            continue

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
        sleep(15)
        system('cls')
        continue

