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


    def atacar(self, personagem):
        personagem.vida -= 20
        print(f'{self.nome} atacou {personagem.nome} e tirou 20 HP.')
        print(f'O personagem atacado agora possui {personagem.vida} HP. \n' if personagem.vida >= 0 else f'Informamos: {personagem.nome} faleceu. \n')


class Guerreiro(Personagem):
    def __init__(self, nome, vida, frase, escudo=False):
        super().__init__(nome, vida, frase) # super() é um método que chama métodos da classe pai
        self.__escudo = escudo

    @property
    def escudo(self):
        return self.__escudo
    
    @escudo.setter
    def escudo(self, escudo):
        self.__escudo = escudo

    # Sobrescrevendo método da classe pai
    def atacar(self, personagem):
        personagem.vida -= 40
        
        print(f'{self.nome} atacou {personagem.nome} e tirou 40 HP.')
        print(f'{personagem.nome}, atacado, agora possui {personagem.vida} HP. \n' if personagem.vida >= 0 else f'Informamos: {personagem.nome} faleceu. \n')

    
    def defender(self, personagem):
        self.__vida += 35


class Mago(Personagem):
    def __init__(self, nome, vida, frase):
        super().__init__(nome, vida, frase) # super() é um método que chama métodos da classe pai

    # Sobrescrevendo método da classe pai
    def atacar(self, personagem):
        personagem.vida -= 6000
        
        print(f'{self.nome} atacou {personagem.nome} e tirou 6000 HP.')
        print(f'O personagem atacado agora possui {personagem.vida} HP. \n' if personagem.vida >= 0 else f'Informamos: {personagem.nome} faleceu. \n')

    
    def curar(self, personagem):
        personagem.vida += 15
        print(f'Personagem {personagem.nome} foi curado por {self.nome}''\n')


fuleco = Personagem('Fuleco', 100, 'AQUI É O BRASIL')
vader = Guerreiro('Darth Vader', 750, 'Eu sou o seu pai')
patolino = Mago('Patolino', 3500, 'O mago é implacável!')

vader.atacar(fuleco)
patolino.curar(fuleco)
fuleco.atacar(patolino)
patolino.atacar(fuleco)
patolino.curar(patolino)


