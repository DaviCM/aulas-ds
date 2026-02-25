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


def add(array):
    system('cls')
    print('Insira as informações do funcionário, para adicionar.')
    nome = (input('Nome: ').title()).strip() 
    sal = getNum('Salário: R$')
    
    array.append({nome : sal})
    
    system('cls')
    print('Usuário adicionado!')
    
    return array


def delete(array):
    removed = False
    
    system('cls')
    print('Insira o nome do funcionário que deseja apagar.')
    nome = (input('Nome: ').title()).strip() 
    
    # [:] cria uma 'shallow copy' da lista 'array', que compartilha propriedades mas significa que não estamos iterando na lista original
    # Iterar na lista original causa erros, pois ao deletar um elemento, os posteriores avançam de index
    # Isso causa um 'pulo' no elemento duas iterações à frente, que passa a ser o próximo, enquanto o da iteração atual é pulado
    # Iterar na cópia garante que os index dela se mantém, mesmo alterando na original.
    # Notação é estranha, mas funciona
    for func in array[:]:
        for key in func:
            if nome == key:
                array.remove(func)
                print('Usuário deletado!')
                print(array)
                sleep(0.5)
                counter += 1
                removed = True

    system('cls')
    print('Todas as instâncias desse usuário foram deletadas.' if removed == True else 'Usuário não encontrado.')
                
    return array
            
funcs = []

while True:
    system('cls')
    print('Bem vindo ao gerenciador de funcionários!')
    print('1 - Visualizar lista')
    print('2 - Adicionar funcionário à lista')
    print('3 - Remover funcionário da lista')
    print('4 - Sair''\n')
    
    opt = input('Insira o que deseja fazer: ').strip()
    
    match opt:
        case '1':
            system('cls')
            print('Funcionários:''\n')
            for func in funcs:
                print(func)
            sleep(3)
            system('cls')
            continue
        
        case '2':
            add(funcs)
            sleep(1)
            system('cls')
            continue
            
        case '3':
            delete(funcs)
            sleep(3)
            system('cls')
            continue
            
        case '4':
            system('cls')
            print('Já vai tarde.')
            break
            
        case _:
            system('cls')
            print('Opção inválida. Reiniciando programa.')
            sleep(0.5)
            continue

