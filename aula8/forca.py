from random import choice
from time import sleep
from os import system
import json

def palavraParaAchar():
    def getInt(value):
        while True:
            try:
                retvalue = value
                retvalue = int(input(retvalue).strip())
                system('cls')

                if (retvalue < 1) or (retvalue > i + 2):
                    raise ValueError
                else:
                    return retvalue

            except ValueError:
                system('cls')
                print('Valor inválido. Tente novamente.')
                sleep(1)
                system('cls')
            
    
    dictKeys = []
    
    with open('aula8/db.json', 'r', encoding='utf-8') as file:
        data = (json.load(file))
    
    for keys in data:
        for key in keys:
            dictKeys.append(key)
    
    while True:
        system('cls')
        print('Bem-Vindo ao Jogo da Forca!')
        
        for i in range(len(dictKeys)): 
            print(f'Opção de jogo {i + 1}: {(dictKeys[i]).title()}')
        print(f'Opção {i + 2}: Sair do Jogo''\n')
    
        opt = getInt('Insira a opção desejada: ')

        if opt == (i + 2):
            system('cls')
            print('Adeus, amigo.')
            return False, None
        else:
            return True, choice(data[opt - 1].get(dictKeys[opt - 1]))


def gameLoop():
    def mainGame():
        valid, palavraAlvo = palavraParaAchar()
        
        if valid == True:
            palavraAlvo = [letra for letra in palavraAlvo]
            palavraEscondida = ['_' for _ in palavraAlvo]
            errors = []
            tries = 6
        
            while True:    
                system('cls')
                print(f'Você possui {tries} erros restantes!')
                print(f'Sua palavra é: {' '.join(palavraEscondida)} \n')
                print(f'Letras descartadas: {errors}' if len(errors) != 0 else 'Nenhuma letra descartada.')
                
                tent = (input('Insira a letra que deseja jogar, ou tente a sorte e insira a palavra inteira: ').lower()).strip()
                
                if len(tent) == 1 and (tent in palavraAlvo):
                    indices = []
                    # enumerate cria um par de chave e valor, que será desempacotado nas variáveis índices (para cada índice da palavra)
                    # e letra, para cada valor.
                    for indices, letra in enumerate(palavraAlvo):
                        if (letra == tent):
                            # Se a letra na palavra alvo for igual ao input, ele substitui o _ na palavra escondida. 
                            # Por causa do for, substituirá em todas as ocorrências
                            palavraEscondida[indices] = tent
                            
                elif len(tent) == 1:
                    errors.append(tent) if tent not in errors else None
                    tries -= 1
                elif (len(tent) > 1) and (tent == ''.join(palavraAlvo)):
                    system('cls')
                    print('Você ganhou, e com ousadia! Parabéns!')
                    print(f'A palavra era: {''.join(palavraAlvo)}')
                    return True
                elif (len(tent) > 1):
                    system('cls')
                    print(f'Você perdeu, mas valeu a ousadia. A palavra era: {''.join(palavraAlvo)}')
                    return True
                else:
                    errors.append(tent) if tent not in errors else None
                    tries -= 1

                if ''.join(palavraEscondida) == ''.join(palavraAlvo):
                    system('cls')
                    print('Você ganhou! Parabéns!')
                    print(f'A palavra era: {''.join(palavraAlvo)}')
                    return True
                        
                if tries == 0:
                    system('cls')
                    print(f'Você perdeu. A palavra era: {''.join(palavraAlvo)}')
                    return True
        else:
            return False
                

    def postGame():
        valid = mainGame()
        
        while valid == True:
            opt = (input('\n''Deseja jogar novamente? (s/n): ').lower()).strip()
            if opt == 's':
                return True
            elif opt == 'n':
                system('cls')
                print('Adeus amigo.')
                return False
            else:
                print('Opção inválida. Tente novamente.')
                sleep(1)
                system('cls')
                continue
        else:
            return False
        
    postGame()
         
gameLoop()
