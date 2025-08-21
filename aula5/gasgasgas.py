from os import system
from time import sleep

def getFloat(value):
    while True:
        try:
            value = float(input(value).replace(',','.'))
            system('cls')
            return value

        except ValueError:
            print('Valor inválido. Tente novamente.')
            sleep(1)
            system('cls')

while True:
    print(f'{5 * '-'} Bem vindo ao calculador de combustível! {5 * '-'}''\n')

    etanol = getFloat('Digite o valor do etanol: ')
    gas = getFloat('Digite o valor da gasolina: ')

    result = (etanol / gas) * 100

    print(f'O valor do etanol é {result:.2f}% do valor da gasolina.')
    print('Abasteça com etanol!' if result <= 75 else 'Abasteça com gasolina!')
        
    quit = (input('\n''Deseja refazer o cálculo? (s/n): ').lower()).strip()

    match quit:
        case 's':
            continue
        case 'n':
            system('cls')
            print('Adeus.')
            break
        case _:
            print('Opção inválida.')
            continue

