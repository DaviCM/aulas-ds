from random import randint

class Personagem:
    def __init__(self, nome, rng, frase, vida):
        self.__nome = nome
        self.__rng = rng
        self.__frase = frase
        self.__vida = vida

    @property
    def nome(self): 
        return self.__nome

    @nome.setter
    def nome(self, novo_nome): 
        self.__nome = novo_nome


    @property
    def rng(self):
        return self.__rng
    
    @rng.setter
    def rng(self, rng):
        self.__rng = rng

        
    @property
    def frase(self):
        return self.__frase
    
    @frase.setter
    def frase(self, nova_frase):
        self.__frase = nova_frase


    @property
    def vida(self): 
        return self.__vida

    @vida.setter
    def vida(self, vida): 
        self.__vida = vida


    def atacar(self, personagem, rng=None, dano=20):
        # Declarar rng como None e atribuir apenas no chamado do método é necessário
        # Caso seja atribuído no método, o rng terá valor fixo para aquele método durante toda a execução
        # E isso é justamente o que o rng busca evitar, portanto tenho que declarar como None
        # E atribuir o valor randômico em cada execução.
        
        if rng == None:
            rng = randint(1, 10000)

        if rng <= 9000:
            personagem.vida -= dano
            print(f'{self.nome} atacou {personagem.nome} e tirou {dano} HP.')
        else:
            print(f'{self.nome} tentou atacar {personagem.nome}, mas falhou. \n')


    def defender(self, personagem, rng=None, escudo=False):
        if rng == None:
            rng = randint(1, 10000)
        
        if escudo == True:
            defenseRNG = rng + 2000
        else:
            defenseRNG = rng

        if defenseRNG > 9000:
            self.__vida += 15
            print(f'{self.nome} conseguiu se defender do ataque!')
            print(f'O dano sofrido por {self.nome} foi reduzido em 15 HP. \n')
        else:
            print(f'{self.nome} tentou defender o ataque de {personagem.nome} e falhou. \n')


    def tomar_elixir(self):
        self.__vida += 20
        print(f'{self.nome} tomou uma poção de vida e recuperou 20 HP.')
        print(f'{self.nome} agora possui {self.vida} HP. \n')

    
    def especial(self, personagem, rng=None):
        if rng == None:
            rng = randint(1, 10000)
        
        print(f'{(self.nome).upper()} ATIVA SEU ESPECIAL!')

        if rng > 9500:
            personagem.vida = 0
            print(f'O ATAQUE FOI BRUTAL! {personagem.nome} foi derrubado. \n')
        else:
            print('O especial falhou. \n')



class Necromante(Personagem):
    def __init__(self, nome, rng=None, frase='O MAGO É IMPLACÁVEL!', vida=75):
        super().__init__(nome, rng, frase, vida)


    def atacar(self, personagem):
        poder = randint(0, 1000)
        print(f'{(self.nome)} conjura os mortos!!!!')
        dano = int(poder * 0.15)
        personagem.vida -= dano
        print(f'{self.nome} atacou {personagem.nome} e tirou {dano} HP.')


    def defender(self, personagem):
        print(f'{(self.nome)} conjura os mortos!!!!')
        super().defender(personagem)


    def tomar_elixir(self):
        super().tomar_elixir()


    def especial(self, personagem):
        super().especial(personagem)



class Ninja(Personagem):
    def __init__(self, nome, rng=None, frase='A constante das sombras...', vida=55):
        super().__init__(nome, rng, frase, vida)


    def atacar(self, personagem, rng=None):
        if rng == None:
            rng = randint(1, 10000)
        
        print(f'{(self.nome)} dispara shurikens de cima do teto!')
        if 5000 < rng <= 9500:
            super().atacar(personagem, rng, dano=30)
            super().atacar(personagem, rng, dano=30)
            print('O bônus de stealth fez o ninja atacar duas vezes!')
        else:
            super().atacar(personagem, rng, dano=30)


    def defender(self, personagem):
        super().defender(personagem)


    def tomar_elixir(self):
        super().tomar_elixir()


    def especial(self, personagem):
        super().especial(personagem)



class Andarilho(Personagem):
    def __init__(self, nome, rng=None, frase='VOU PEGAR MINHA MARREEEEEEETA!', vida=120):
        super().__init__(nome, rng, frase, vida)


    def atacar(self, personagem):
        print(f'{(self.nome)} ataca com sua faca de cozinha!')
        super().atacar(personagem)


    def defender(self, personagem):
        print(f'{(self.nome)} se defende bravamente com seu escudo!')
        super().defender(personagem, escudo=True)


    def tomar_elixir(self):
        super().tomar_elixir()


    def especial(self, personagem):
        super().especial(personagem)
        
