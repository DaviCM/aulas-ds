from os import system
from time import sleep

def getFloat(value):
    while True:
        try:
            value = float(input(value).strip())
            system('cls')
            return value

        except ValueError:
            print('Valor inválido. Tente novamente.')
            sleep(1)
            system('cls')
            continue

num = getFloat('Insira um número: ')
print(f'O valor absoluto dele é: {abs(num)}')

