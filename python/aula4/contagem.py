from time import sleep
from os import system

cont = input('Digite um número inteiro: ')

while True:
    try:
        cont = int(cont)
    except ValueError:
        print('Valor inválido. Tente novamente!''\n')
        continue

    print(f'Contagem regressiva: {cont}')
    sleep(0.1)
    cont -= 1
    system('cls')
    if cont == 0:
        break
    

print('\n''CABOOOOOOO! É TETRA! É TETRA!')


