from random import uniform
from time import sleep
from os import system

aposta = float(input('Digite o valor da sua aposta: R$').replace(',','.'))
counter = 1

while True:
    xpo = 1 + (uniform(0.01,0.0001))
    counter *= xpo
    print(f'Valor multiplicado em: x{(counter):.3f}')

    aposta = aposta * (xpo)
    print(f'O valor da aposta é: R${aposta:.2f}')

    sleep(0.1)
    system('cls')

