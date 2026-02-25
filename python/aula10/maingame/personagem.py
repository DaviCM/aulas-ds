from random import randint, choice
from time import sleep
from os import system
from classes import *

def pegarSTR(inputmsg, errormsg):
    while True:
        string = (input(inputmsg)).strip()
        if string == '':
            system('cls')
            print(errormsg)
            sleep(0.5)
            system('cls')
            continue
        else:
            return string
    
    
# __subclasses__() é um método de classes python, que retorna uma lista com as subclasses da determinada classe.
# Usar na classe Personagens nos permite ver e alocar dinamicamente no menu todas as suas subclasses.
# Dá pra acessar e usar funções em seus valores normalmente com [], como em uma lista qualquer.
def get_actors():
    while True:
        system('cls')
        print('----- Bem vindo ao grande RPG! ----- \n')
        
        for num, cls in enumerate(Personagem.__subclasses__(), start=1):
            print(f'Opção {num}: {cls.__name__}')
        print('\n'f'Opção {num + 1}: Sair do jogo.')

        opt = input('\n''Escolha qual herói você será hoje: ').strip()

        try:
            opt = int(opt)
            if opt < 1 or opt > (len(Personagem.__subclasses__()) + 1):
                raise ValueError
            
        except ValueError:
            system('cls')
            print('Valor inválido. Por favor, tente novamente.')
            sleep(0.5)
            continue

        sleep(0.1)
        system('cls')
        
        if opt == (num + 1):
            system('cls')
            print('Que pena, até a próxima! (menu principal)')
            return None, None
        else:
            player_class = Personagem.__subclasses__()[opt - 1]
            print(f'Você será um grande {player_class.__name__}! \n')
            player_name = pegarSTR('Digite seu nome: ', 'Nome inválido. Digite outro!').title()
            player_frase = pegarSTR('Digite sua frase de efeito: ', 'Frase de efeito inválida. Digite outra!')
            
            
            # Retorna a classe instanciada com os atributos do jogador
            player = player_class(player_name, player_frase)
            
            # Escolhe aleatóriamente uma das classes de inimigos, e instancia seu nome como o objeto 'enemy'
            # Assim, podemos chamar 'enemy.método()' em todos os métodos das subclasses
            enemy_class = (choice(Personagem.__subclasses__()))
            
            # Tenho que colocar no enemy_class() para colocar o nome como sendo instância da classe, caso contrário será str
            # Igual instanciar uma classe no código normal
            enemy = enemy_class(enemy_class.__name__) # Pode ser 'Necromante', 'Ninja' ou 'Andarilho' - E é escalável para adicionar outras classes
            
            return player, enemy
        
            # Código, ao ver 'enemy.atacar(player), irá acessar a variável enemy, que terá o nome dado para o objeto (nome da subclasse escolhida), e utilizará ele para chamar o método certo.
    

def game_loop():
    player, enemy = get_actors()
    
    if player != None and enemy != None:
        print(f'Player: {player.nome}, Enemy: {enemy.nome}')

        while True:
            system('cls')
            print(f'{enemy.nome}: {enemy.vida} HP')
            print(f'{player.nome}: {player.vida} HP \n')
            
            print('1 - Atacar')
            print('2 - Defender')
            print('3 - Beber Elixir ')
            print('4 - Usar Especial \n')
            opt = input('Escolha o que deseja fazer: ').strip()
            system('cls')
            
            match opt:
                case '1':
                    player.atacar(enemy)
                    sleep(5)
                    system('cls')
                case '2':
                    player.defender(enemy)
                    sleep(5)
                    system('cls')
                case '3':
                    player.tomar_elixir()
                    sleep(5)
                    system('cls')
                case '4':
                    player.especial(enemy)
                    sleep(5)
                    system('cls')
                case _:
                    print('Opção inválida. Tente novamente')
                    sleep(0.5)
                    continue
            
            if enemy.vida <= 0:
                print(f'{enemy.nome} foi derrotado. Parabéns!')
                print(f'{player.nome} wins.')
                sleep(5)
                return True
            
            # Lista as ações do inimigo em uma lista e pega seu nome com choice, para depois executar a função correta.
            enemy_turn = choice([enemy.atacar, enemy.defender, enemy.tomar_elixir, enemy.especial])
            enemy_turn(player) if enemy_turn != enemy.tomar_elixir else enemy_turn()
            sleep(5)
            system('cls')
            
            if player.vida <= 0:
                print(f'Você, {player.nome}, foi derrotado. Meus pêsames.')
                print(f'{enemy.nome} wins.')
                sleep(5)
                return True
            else:
                continue
            
    else:
        return False

                 
def post_game():
    valid_game = game_loop()
    
    while valid_game == True:
        opt = (input('Deseja jogar novamente? (s/n): ').lower()).strip()
        system('cls')
    
        match opt:
            case 's':
                print('Retornando ao menu principal!')
                sleep(0.5)
                valid_game = game_loop()
            case 'n':
                print('Que pena. Até a próxima! (pós-jogo)')
                break
            case _:
                print('Opção inválida. Tente novamente.')
                continue


# Inútil nessa situação, mas tá valendo - código não vai ser importado em nenhum outro lugar
if __name__ == '__main__':
    post_game()

