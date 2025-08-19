from os import system
from time import sleep

soma = 0
notas = []

def getInt(value):
    while True:
        try:
            value = int(input(value))
            system('cls')
            return value

        except ValueError:
            print('Valor inválido. Tente novamente.')
            sleep(2)
            system('cls')
            continue
            

while True:
    print(f'{5 * '-'} Bem vindo ao grande gerenciador de notas! {5 * '-'}')
    qtdnotas = getInt('Insira quantas notas esse aluno possui: ')

    
    for i in range(qtdnotas):
        nota = getInt(f'Digite a {i + 1}° nota: ')
        notas.append(nota)
        
    media = sum(notas) / qtdnotas

    system('cls')
    for i in range(len(notas)):
        print(f'A {i + 1}° nota do aluno é: {notas[i]}')
    
    print(f'A média desse cara é: {media}')

    quit = input('Deseja calcular a média novamente? (n para sair): ')
    if quit == 'n':
        system('cls')
        print('Já vai tarde.')
        break
    else:
        system('cls')
        continue


