from random import uniform, randint
from time import sleep
from os import system

print(f'{8 * '-'} Bem vindo ao Tigrinho! {8 * '-'}''\n')

aposta = float(input('Digite o valor da sua aposta: R$').replace(',','.'))
counter = 1

while True:
    if aposta >= 65:
        xpo = xpo = 1 + (uniform(0.001,0.0001))
    else:
        xpo = 1 + (uniform(0.01,0.0001))
        
    counter *= xpo
    print(f'Valor multiplicado em: x{(counter):.3f}')

    aposta *= xpo
    print(f'O valor da aposta é: R${aposta:.2f}')
    sleep(0.1)
    system('cls')
    
    if randint(0,100000) >= 99000 and counter > 1.05:
        print(f'Valor multiplicado em: x{(counter):.3f}')
        print(f'O valor da aposta é: R${aposta:.2f}')
        print('\n'f'{5 * '-'} VOCÊ PERDEU! OBRIGADO PELO DINHEIRO! {5 * '-'}')
        break



    