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
print('Bem vindo ao conversor de horas para minutos!''\n')

hr = getInt('Digite o valor que deseja converter: ')
print(f'Esse horário corresponde a {hr * 60} minutos!')

