from random import randint
from os import system

rand = randint(1,100)
max = 10
tentativas = 0

system('cls')
print(f'{5 * '-'} Bem vindo ao gameshow! {5 * '-'}')
print(f'Você tem {max} tentativas para acertar o valor certo entre 1 e 100!')

while (tentativas <= max) and (max - tentativas > 0):
    try:
        usernum = int(input('\n''Insira o seu número: '))
        tentativas += 1
        system('cls')
    except ValueError:
        print('Valor não é inteiro. Tente novamente.')
        continue
    
    if usernum == rand: # Davi: Eu não faço ideia do que isso aqui faz
        print('Meu Deus! Você é um mago da matemática!')
        print(f'O valor certo era {rand} e você acertou em {tentativas} tentativas!')
        break
    elif usernum > rand:
        print('Tente novamente. Dica: o valor é menor.')
        print(f'Você tem {max - tentativas} tentativas!')
        continue
    else:
        print('Tente novamente. Dica: o valor é maior.')
        print(f'Você tem {max - tentativas} tentativas!')
        continue

else:    
    print(f'Que pena, você perdeu. O valor certo era {rand}.')

