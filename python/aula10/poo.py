# Classe - descrição de um 'formato geral' que os objetos devem ter
# Atributos - as variáveis da classe, que são únicas para cada instância dela (características do objeto)
# Métodos - Funções, as ações que os objetos podem realizar

# self - 'nome da classe', porém referido apenas dentro dela mesma - usado para referenciar atributos de dentro.
# construtor - necessário para acessar os atributos da classe, ao criar um objeto.
# construtor é o __init__

# Os atributos podem ser encapsulados como:
# public - atributo público, pode ser acessado por todas as classes (sem underscore)
# private - atributo encapsulado e contido em uma única classe (__ antes do nome) - não será possível chamar a porpriedade diretamente.
# protect - envia um 'sinal de captura' para o acesso por outra classe ser permitido (_ antes do nome)

# @property - decorador que remove parênteses do chamado e retorna o valor que foi dado para o atributo
# '__nome' e '__vida' no nosso init irão chamar nosso método getter para atualizar os atributos
# @atributo.setter - recebe o valor do getter no atributo da classe.

# Caminho do atributo: atribuição (criação do obj) - construtor - getter - setter
# A setter recebe o valor que foi atribuido na criação do objeto e iguala ele ao atributo.

class Personagem:
    def __init__(self, nome, vida, frase):
        # colocando os parâmetros inseridos dentro da classe, com o self.
        self.__nome = nome
        self.__vida = vida
        self.__frase = frase

    # getter de '__nome'
    @property
    def nome(self): 
        return self.__nome

    # setter de '__nome'
    @nome.setter
    def nome(self, novo_nome): 
        self.__nome = novo_nome

    # getter de '__vida'
    @property
    def vida(self): 
        return self.__vida

    # setter de '__vida'
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
        print(f'O personagem atacado agora possui {personagem.vida} HP.''\n')
        print(f'Personagem atacante diz: {self.frase}')
        print(f'Personagem atacado diz: {personagem.frase}')

p1 = Personagem('Darth Vader', 750, 'Eu sou o seu pai!')
p2 = Personagem('Silvio Santos', 125, 'Maoe, Quem quer dinheiro?')

p1.atacar(p2)

