from time import sleep
from os import system

def getNum(value):
    while True:
        try:
            value = float(input(value).strip())
            return value
        
        except ValueError:
            system('cls')
            print('Valor inválido. Tente novamente.')
            sleep(1)
            system('cls')
            continue


def create_update(dicio):
    system('cls')
    print('Insira o nome do produto que deseja adicionar ou atualizar.')
    nome = (input('Nome: ').title()).strip()
    
    
    if nome in dicio.keys():
        prec = dicio[nome]['Preço']
        qtd = dicio[nome]['Qtd. Disponível']
    
        while True:
            system('cls')
            print(f'{nome} já está nesse mercado. Opções disponíveis: ')
            print('1 - Alterar preço')
            print('2 - Alterar quantidade disponível')
            print('3 - Excluir produto')
            print('4 - Voltar''\n')
            opt = input('Insira o que deseja fazer: ').strip()
            
            
            system('cls')
            
            match opt:
                case '1':
                    while True:
                        prec = getNum(f'Insira o novo preço do produto {nome} R$: ')
                        system('cls')
                        print('Preço atualizado!')
                        sleep(0.5)
                        break
                
                case '2':
                    while True:
                        prec = getNum(f'Insira a quantidade de {nome} disponível: ')
                        system('cls')
                        print('Quantidade atualizada!')
                        sleep(0.5)
                        break
                        
                case '3':
                    while True:
                        delete = (input(f'Tem certeza que deseja excluir {nome}? (s/n):').lower()).strip()
                        
                        if delete == 's':
                            del dicio[nome]
                            break
                        elif delete == 'n':
                            print('Retornando ao menu principal.')
                            sleep(0.5)
                            break
                        else:
                            print('Resposta inválida. Tente novamente.')
                            sleep(0.5)
                            continue

                case '4':
                    system('cls')
                    print('Retornando ao menu principal.')
                    sleep(0.5)
                    break
                    
                case _:
                    system('cls')
                    print('Opção inválida. Reiniciando programa.')
                    sleep(0.5)
                    continue
    else:
        prec = getNum('Insira o valor do produto: ')            
        qtd = getNum('Insira a quantidade disponível: ')
        system('cls')           
    
    dicio.update({nome : {'Preço' : prec, 'Qtd. Disponível' : qtd}})
        
    system('cls')
    print(f'{dicio}')
        
    return dicio

prods : dict = {}

while True:
    system('cls')
    print('Bem vindo ao gerenciador de funcionários!')
    print('1 - Visualizar lista de produtos')
    print('2 - Adicionar ou atualizar produtos')
    print('3 - Sair''\n')
    
    opt = input('Insira o que deseja fazer: ').strip()
    
    match opt:
        case '1':
            system('cls')
            print('Produtos:''\n')
            
            for prod in prods:
                print(f'{prod} : {prods.get(prod)}')
                
            sleep(3)
            system('cls')
            continue
        
        case '2':
            create_update(prods)
            sleep(1)
            system('cls')
            continue
            
        case '3':
            system('cls')
            print('Já vai tarde.')
            break
            
        case _:
            system('cls')
            print('Opção inválida. Reiniciando programa.')
            sleep(0.5)
            continue

