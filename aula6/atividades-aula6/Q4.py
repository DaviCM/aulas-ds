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

values = []

system('cls')

for i in range(3):
    num = getFloat('Digite um valor: ')
    values.append(num)

print(f'A média entre os três valores é: {(sum(values) / 3)}')


