from random import choice
from os import system
from time import sleep

lista_nm = []
sorteados = []

while True:
    system('cls')
    nome = (input('Digite o nome do cabra (n para sair): ').strip()).capitalize()
    lista_nm.append(nome)

    if (nome != 'N') and (len(lista_nm) > 1):
        print(f'{5 * '-'} Adicionado! {5 * '-'}''\n')

        print(lista_nm)

        sort = (input('Deseja sortear? (s/n)').strip()).lower()

        if sort == 'n':
            continue
        else:
            escolhido = choice(lista_nm)
            sorteados.append(escolhido)
            lista_nm.remove(escolhido)
            print(f'O sorteado foi: {escolhido}!')
            sleep(5)

    elif (nome != 'N') and (len(lista_nm) <= 1):
        print(f'{5 * '-'} Insira ao menos mais um nome! {5 * '-'}''\n')
        sleep(1)
        continue

    else:
        print('Já vai tarde.')
        break


print(f'Os sorteados foram: {sorteados}')




