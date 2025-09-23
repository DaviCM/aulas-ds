from random import randint
from time import sleep
from os import system

class Personagem:
    def __init__(self, nome, vida, frase):
        self.__nome = nome
        self.__vida = vida
        self.__frase = frase

    @property
    def nome(self): 
        return self.__nome

    @nome.setter
    def nome(self, novo_nome): 
        self.__nome = novo_nome

    @property
    def vida(self): 
        return self.__vida

    @vida.setter
    def vida(self, vida): 
        self.__vida = vida

    @property
    def frase(self):
        return self.__frase
    
    @frase.setter
    def frase(self, nova_frase):
        self.__frase = nova_frase


    def endTurn(self):
        turnRNG = randint(1, 10000)
        return turnRNG


    def atacar(self, personagem, dano=20):
        turnRNG = self.endTurn()

        if turnRNG <= 5000:
            personagem.vida -= dano
            print(f'{self.nome} atacou {personagem.nome} e tirou {dano} HP.')
            print(f'O personagem atacado agora possui {personagem.vida} HP. \n' if personagem.vida >= 0 else f'Informamos: {personagem.nome} faleceu. \n')
        else:
            print(f'{self.__nome} tentou atacar {personagem.nome}, mas falhou. \n')


    def defender(self, personagem, escudo=False):
        turnRNG = self.endTurn()

        if escudo == True:
            defenseRNG = turnRNG - 1000
        else:
            defenseRNG = turnRNG

        if defenseRNG > 5000:
            print(f'{self.__nome} conseguiu se defender do ataque! \n')
        else:
            print(f'{self.__nome} tentou defender o ataque de {personagem.nome} e falhou. \n')


    def tomar_elixir(self):
        turnRNG = self.endTurn()

        self.__vida += 30
        print(f'{self.__nome} tomou uma poção de vida e recuperou 30 HP.')
        print(f'O personagem agora possui {self.__vida} HP. \n')

    
    def especial(self, personagem):
        turnRNG = self.endTurn()

        print(self.__frase)

        if turnRNG > 7500:
            personagem.vida -= personagem.vida
            print(f'O ATAQUE FOI BRUTAL! {personagem.nome} foi derrubado. \n')
        else:
            print('O especial falhou. \n')



class Necromante(Personagem):
    def __init__(self, nome, vida, frase):
        super().__init__(nome, vida, frase)


    def atacar(self, personagem, poder=randint(0, 1000)):
        print(f'{(self.__nome)} conjura os mortos!!!!')
        dano = int(poder * 0.35)
        personagem.vida -= dano
        print(f'{personagem.nome} sofreu {dano} dano. Seu HP é {personagem.vida}')


    def defender(self, personagem):
        print(f'{(self.__nome)} conjura os mortos!!!! \n')
        super().defender(personagem)


    def tomar_elixir(self):
        super().tomar_elixir()


    def especial(self, personagem):
        print(f'{(self.__nome).upper} CONJURA MILHÕES DE ESQUELETOS, VINDOS DIRETAMENTE DO INFERNO!')
        super().especial(personagem)



class Ninja(Personagem):
    def __init__(self, nome, vida, frase):
        super().__init__(nome, vida, frase)


    def atacar(self, personagem):
        turnRNG = self.endTurn()

        print(f'{(self.__nome)} dispara shurikens de cima do teto!')
        if turnRNG > 6000:
            super().atacar(personagem, dano=30)
            super().atacar(personagem, dano=30)
            print('O bônus de stealth fez o ninja atacar duas vezes!')
        else:
            super().atacar(personagem, dano=30)


    def defender(self, personagem):
        super().defender(personagem)


    def tomar_elixir(self):
        super().tomar_elixir()


    def especial(self, personagem):
        print(f'{(self.__nome).upper} SACA SUA KATANA NA VELOCIDADE DA LUZ!')
        super().especial(personagem)



class Campones(Personagem):
    def __init__(self, nome, vida, frase):
        super().__init__(nome, vida, frase)


    def atacar(self, personagem):
        print(f'{(self.__nome)} ataca com sua faca de cozinha!')
        super().atacar(personagem)


    def defender(self, personagem):
        print(f'{(self.__nome)} se defende bravamente com seu escudo!')
        super().defender(personagem, escudo=True)


    def tomar_elixir(self):
        super().tomar_elixir()


    def especial(self, personagem):
        print(f'{(self.__nome).upper} APITA E CHAMA SEU EXÉRCITO DE TOUROS!')
        super().especial(personagem)



pers = ['Necromante', 'Ninja', 'Camponês']

def main():
    while True:
        system('cls')
        print('Bem vindo ao grande RPG!')
        for num, classname in enumerate(pers, start=1):
            print(f'Opção {num}: {classname}')

        opt = input('\n''Escolha qual herói você será hoje: ').strip()

        try:
            opt = int(opt)
        except ValueError:
            print('Valor inválido. Por favor, tente novamente.')
            sleep(0.5)
            continue

        if opt <= num:
            print(f'Você será um grande {pers[opt - 1]}!')
            break
        else:
            print('Escolha uma opção válida.')
            sleep(0.5)
            continue



main()


