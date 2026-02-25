from os import system
from time import sleep

soma = 0
notas = []

def getInt(value):
    while True:
        try:
            retValue = int(input(value))
            if retValue >= 0 and retValue <= 10:
                system('cls')
                return retValue
            else:
                raise ValueError

        except ValueError:
            print('Valor inválido. Tente novamente.')
            sleep(1)
            system('cls')
            continue
            

while True:
    print(f'{5 * '-'} Bem vindo ao grande gerenciador de notas! {5 * '-'}')
    qtdnotas = getInt('Insira quantas notas esse aluno possui: ')
 
    for i in range(qtdnotas):
        nota = getInt(f'Digite a {i + 1}° nota (0-10): ')
        notas.append(nota)
        
    media = sum(notas) / qtdnotas

    system('cls')
    for i in range(len(notas)):
        print(f'A {i + 1}° nota do aluno é: {notas[i]}')
    
    print(f'A média desse cara é: {media}')

    if media >= 7:
        print('Aprovado.')
    elif media >= 5 and media < 7:
        print('Boa recuperação.')
    else:
        print('Se ferrou.')

    quit = input('\n''Deseja calcular a média novamente? (n para sair): ')

    if quit == 'n':
        system('cls')
        print('Já vai tarde.')
        break
    else:
        system('cls')
        continue


