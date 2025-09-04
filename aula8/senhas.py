from random import choice
from time import sleep
from os import system
import string

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


def novaSenha(length=12, upperC=True, lowerC=True, number=True, special=True):

    pwOptions = ''

    # Métodos do módulo string que retornam um tipo específico de caractere
    if upperC == True:
        pwOptions += string.ascii_uppercase

    if lowerC == True:
        pwOptions += string.ascii_lowercase

    if number == True:
        pwOptions += string.digits

    if special == True:
        pwOptions += string.punctuation

    pw = ''.join(choice(pwOptions) for _ in range(length))

    return pw


qtdsenhas = getInt('Digite quantas senhas você deseja gerar: ')
pwLength = getInt('Digite o tamanho das senhas (enter para padrão 12): ')

useUpper = True if (input('Deseja que a senha tenha caracteres maiúsculos? (n para negar): ').lower()).strip() != 'n' else False
useLower = True if (input('Deseja que a senha tenha caracteres minúsculos? (n para negar): ').lower()).strip() != 'n' else False
useNumber = True if (input('Deseja que a senha tenha números? (n para negar): ').lower()).strip() != 'n' else False
useSpecial = True if (input('Deseja que a senha tenha caracteres especiais? (n para negar): ').lower()).strip() != 'n' else False

# With: Bloco que opera um código e automaticamente finaliza a operação ao fim.
with open('aula8/senhas.txt', 'w', encoding='utf-8') as file:
    for i in range(qtdsenhas):
        file.write(f'{i + 1}° senha: {novaSenha(pwLength, useUpper, useLower, useNumber, useSpecial)} \n\n')

    sleep(1)
    system('cls')
    print('As senhas foram adicionadas ao arquivo!')

