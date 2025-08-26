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


x = getInt("Digite o numero da tabuda: ")
for num in range(1, 11):
    print(f'{x} X {num} = {x * num}')

