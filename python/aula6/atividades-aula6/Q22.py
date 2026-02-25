from os import system
from time import sleep

def getInt(value):
    while True:
        try:
            value = int(input(value).strip())
            system('cls')
            return value

        except ValueError:
            print('Valor inválido. Tente novamente.')
            sleep(1)
            system('cls')
            continue

system('cls')

dist = getInt('Insira a distância que você percorreu (KM): ')
gas = getInt('Insira a quantidade de combustível que foi gasto (L): ')

print(f'A média de consumo foi: {(dist / gas):.2f} km / L')


