from random import choice
from time import sleep
from os import system
import json

def getKeys():
    dictKeys = []
    
    with open('aula8/db.json', 'r', encoding='utf-8') as file:
        data = (json.load(file))
    
    for keys in data:
        for key in keys:
            dictKeys.append(key)
    
    return data, dictKeys


def createGame():
    data, dictKeys = getKeys()
    newValues = []
    counter = 1
        
    while True:
        system('cls')
        print('Bem vindo ao criador de categorias!''\n')
         
        category = (input('Insira o nome da categoria desejada: ').lower()).strip()
        
        if (category in dictKeys) or (category == ' '):
            system('cls')
            print('Esse nome já foi utilizado ou é inválido. Insira outro.')
            sleep(1)
            continue
        
        while True:
            system('cls')
            name = (input(f'Insira a {counter}° opção da categoria (enter para finalizar): ').lower()).strip()
            if name == '':
                break
            else:
                newValues.append(name)
                counter += 1
        break
    
    valuesDict = {category : newValues}
    data.append(valuesDict)
    
    print('\n'f'Nova categoria adicionada: {valuesDict}')
    sleep(1)
    system('cls')
                
    with open('aula8/db.json', 'w', encoding='utf-8') as file:
        # data = dicionário atualizado, file = arquivo onde será adicionado, ensure_ascii=false para permitir outros caracteres, indent=4 para organização com tab.
        json.dump(data, file, ensure_ascii=False, indent=4)
        
    
def getWord():
    while True:
        data, dictKeys = getKeys()
    
        system('cls')
        print(f'{5 * '-'} Bem-Vindo ao Jogo da Forca! {5 * '-'}''\n')
        
        for i in range(len(dictKeys)): 
            print(f'Opção de jogo {i + 1}: {(dictKeys[i]).title()}')
        print('\n'f'Opção {i + 2}: Criar nova categoria de jogo')
        print(f'Opção {i + 3}: Sair do Jogo''\n')

        try:
            opt = int(input('Insira a opção desejada: '))
            if (opt < 1) or (opt > (i + 3)):
                raise ValueError

        except ValueError:
            system('cls')
            print('Valor inválido. Por favor, tente novamente.')
            sleep(1)
            continue

        if (opt >= 1) and (opt < (i + 2)):
            # Valor de retorno usa a função get no conjunto de dados total, que retorna o dicionário correto. Então, pegamos as keys do dicionário
            # Armazenadas em dictKeys, e usamos como parâmetro no get.
            return True, choice(data[opt - 1].get(dictKeys[opt - 1]))
        elif opt == (i + 2):
            createGame()
            continue
        elif opt == (i + 3):
            system('cls')
            print('Adeus, amigo (Opção de sair).')
            return False, None


def gameLoop():  
    def mainGame():
        valid, palavraAlvo = getWord()
        
        if valid == True:
            errors = []
            palavraEscondida = []
            tries = 6
            palavraAlvo = [letra for letra in palavraAlvo]

            for s in palavraAlvo:
                if s == ' ':
                    palavraEscondida.append(' ')
                else:
                    palavraEscondida.append('_')

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
                    print(f'A resposta era: {''.join(palavraAlvo)}')
                    return True
                elif (len(tent) > 1):
                    system('cls')
                    print(f'Você perdeu, mas valeu a ousadia. A resposta era: {''.join(palavraAlvo)}')
                    return True
                else:
                    errors.append(tent) if tent not in errors else None
                    tries -= 1

                if ''.join(palavraEscondida) == ''.join(palavraAlvo):
                    system('cls')
                    print('Você ganhou! Parabéns!')
                    print(f'A resposta era: {''.join(palavraAlvo)}')
                    return True
                        
                if tries == 0:
                    system('cls')
                    print(f'Você perdeu. A resposta era: {''.join(palavraAlvo)}')
                    return True
        else:
            return False
                

    def postGame():
        valid = mainGame()
        
        while valid == True:
            opt = (input('\n''Deseja jogar novamente? (s/n): ').lower()).strip()
            
            if opt == 's':
                valid = mainGame()
            elif opt == 'n':
                system('cls')
                print('Adeus amigo (Recusa a jogar novamente).')
                break
            else:
                print('Opção inválida. Tente novamente.')
                sleep(1)
                system('cls')
                continue
     
             
    postGame()

         
gameLoop()







