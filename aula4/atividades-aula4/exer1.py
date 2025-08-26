from os import system
from time import sleep

nomes = []


def endChoice():
    sleep(1)
    system('cls')
    
    
def getInt(value):
    while True:
        try:
            value = int(input(value))
            system('cls')
            return value

        except ValueError:
            print('Valor inválido. Tente novamente.')
            endChoice()
            break


while True:
    print(f'{5 * '-'} Bem vindo ao grande gerenciador de listas! {5 * '-'}')
    sleep(0.5)
    print('1 - Visualizar lista')
    print('2 - Adicionar elemento à lista')
    print('3 - Remover elemento da lista')
    print('4 - Ordenar a lista')
    print('5 - Pesquisar elemento da lista')
    print('6 - Ir embora')
    
    choice = getInt('Escolha a opção que deseja: ')
    
    if choice < 1 or choice > 6:
        print('Valor inválido. Tente novamente.')
        endChoice()
        continue
    
    elif choice == 1:
        print('1 - Visualizar lista''\n')
        
        print(f'Sua lista é: {nomes}')
        sleep(4)
        endChoice()
        continue
        
    elif choice == 2:
        print('2 - Adicionar elemento à lista''\n')
        novo = input('Digite o nome que deseja adicionar: ').capitalize()
        
        position = (input('Deseja adicionar em uma posição específica? (s/n): ').strip()).lower()

        if position == 'n':
            print(f'{novo} será adicionado ao final da lista.')
            nomes.append(novo)
            endChoice()
            continue
            
        elif position == 's':
            print(f'A sua lista possui {len(nomes)} posições.')
            insertion = getInt('Escolha a posição desejada: ')
            
            if insertion > len(nomes):
                print('Posição inválida. Reiniciando sistema.')
                endChoice()
                continue
            else:
                nomes.insert(insertion - 1, novo)
                print(f'Adicionando {novo} na {insertion}° posição!')
                endChoice()
                continue
        
        else:
            print('Resposta inválida. Reiniciando sistema.')
            endChoice()
            continue
    
    elif choice == 3:
        print('3 - Remover elemento da lista''\n')
        
        print(f'A sua lista possui os elementos: {nomes}.')
        try:
            deletion = input('Escolha um elemento para remover: ').capitalize()
            nomes.remove(deletion)
            print(f'Removendo {deletion} da lista.')
        except ValueError:
            print('Valor não encontrado. Reiniciando.')
        endChoice()
        continue
        
    elif choice == 4:
        print('4 - Ordenar a lista''\n')
        print(f'A sua lista possui os elementos: {nomes}.')
        print('\n''Opções para ordenar lista: ''\n')
        
        print('1 - Ordenar em ordem crescente')
        print('2 - Ordenar em ordem decrescente')
        
        order = getInt('Escolha a opção que deseja: ')
        
        if order < 1 or order > 2:
            print('Valor inválido. Tente novamente.')
            endChoice()
            continue
        
        elif order == 1:
            print('Sorteando em ordem crescente!')
            nomes.sort()
            endChoice()
            continue
        
        elif order == 2:
            print('Sorteando em ordem decrescente!')
            nomes.sort(reverse=True)
            endChoice()
            continue
        
    elif choice == 5:
        print('5 - Pesquisar elemento da lista''\n')
        search = input('Escreva o nome que deseja pesquisar: ')
        try:
            print(f'O nome {search} aparece na lista! Posição: {nomes.index(search) + 1}')
        except ValueError:
            print('Valor não encontrado an lista.')
        endChoice()
        continue
    
    elif choice == 6:
        print('6 - Ir embora''\n')
        print('Já vai tarde.')
        break
        
