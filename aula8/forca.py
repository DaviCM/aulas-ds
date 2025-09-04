from random import choice
from time import sleep
from os import system

def palavraParaAchar():
    opts = ['python', 'developer', 'programação', 'inteligência', 'artificial', 'computador',
            'java', 'javascript', 'garoto', 'programa', 'notebook', 'computador', 'memória',
            'sistema', 'operacional', 'monitor', 'samsung', 'palavras', 'escola', 'anime',
            'forca', 'gabinete', 'placa', 'teclado', 'calvície', 'laptop', 'desktop', 'hardware']
    
    return choice(opts)


def gameLoop():

    palavraAlvo = [letra for letra in palavraParaAchar()]
    palavraEscondida = ['_' for _ in palavraAlvo]
    errors = []
    tries = 6

    tent = (input('Insira a letra que deseja jogar, ou tente a sorte e insira a palavra inteira: ').lower()).strip()

    if len(tent) == 1 and (tent in palavraAlvo):
        indices = []
        # enumerate cria um par de chave e valor, que será desempacotado nas variáveis índices (para cada índice da palavra)
        # e letra, para cada valor.
        for indices, letra in enumerate(palavraAlvo):
            if (letra == tent) and (tent not in palavraEscondida):
                # Se a letra na palavra alvo for igual ao input, ele substitui o _ na palavra escondida. 
                # Por causa do for, substituirá em todas as ocorrências
                palavraEscondida[indices] = tent
    elif len(tent) == 1:
        errors.append(tent)
        tries -= 1
    elif (len(tent) > 1) and (tent == ''.join(palavraAlvo)):
        system('cls')
        print('Você ganhou, e com ousadia! Parabéns!')
        print(f'A palavra era: {''.join(palavraAlvo)}')
    elif len(tent) > 1:
        system('cls')
        print(f'Você perdeu, mas valeu a ousadia. A palavra era: {''.join(palavraAlvo)}')
    else:
        errors.append(tent)
        tries -= 1

    if ''.join(palavraEscondida) == ''.join(palavraAlvo):
        system('cls')
        print('Você ganhou! Parabéns!')
        print(f'A palavra era: {''.join(palavraAlvo)}')
        
    if tries == 0:
        system('cls')
        print(f'Você perdeu. A palavra era: {''.join(palavraAlvo)}')

    while True:
        system('cls')
        print(f'Você possui {tries} tentativas restantes!')
        print(f'Sua palavra é: {' '.join(palavraEscondida)} \n')
        print(f'Letras descartadas: {errors}' if len(errors) != 0 else 'Nenhuma letra descartada.')

gameLoop()


