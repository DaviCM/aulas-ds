from os import system
from time import sleep

def getInt(value):
    while True:
        try:
            value = int(input(value))
            system('cls')
            return value

        except ValueError:
            if value == '':
                system('cls')
                return value
            
            else:
                print('Valor inválido. Tente novamente.')
                sleep(1)
                system('cls')
                continue


n = 1
values = []

while True:
    system('cls')
    print(f'{5 * '-'} Bem vindo ao Numeros Infinitos! {5 * '-'}')
    usernum = getInt(f'Digite o {n}° valor ou enter para ver todos: ')
    
    if usernum != '':
        values.append(usernum)
        n += 1
    
    else:
        print('Esses são seus valores em ordem crescente:')
        values.sort()
        print(values)
        break
    
    