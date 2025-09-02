import json
from os import system, name, path
from time import sleep

users = []

# É assim que se declara uma lambda!
clear = lambda: system('cls' if name == 'nt' else 'clear')

# Função escrita por mim, que checa se um valor é int e pega o dado novamente se ocorrer um erro.
def getInt(value):
    while True:
        try:
            value = int(input(value).strip())
            clear()
            return value

        except ValueError:
            print('Valor inválido. Tente novamente.')
            sleep(1)
            clear()
            continue


while True:
    # Dicionário ficará vazio a cada iteração, para adicionar um novo usuário à lista 'users'.
    newuser = {}

    print(f'{5*'-'} Bem vindo ao manipulador de JSON! {5*'-'}')

    print('1 - Cadastrar novo usuário')
    print('2 - Salvar arquivo JSON')
    print('3 - Fazer leitura do JSON')
    print('4 - Ir embora''\n')

    opt = getInt('Escolha a ação desejada: ')

    match opt:
        case 1:
            clear()

            # Aqui eu adiciono as chaves nome, idade e email ao dicionário do usuário
            newuser['nome'] = (input('Digite o nome do usuário: ').title()).strip()
            newuser['idade'] = getInt('Digite a idade do usuário: ')
            newuser['email'] = input('Digite o email do usuário: ').strip()

            users.append(newuser)
            print('Dados adicionados ao banco. Adicione agora ao JSON.')
            sleep(1)
            clear()

        case 2:
            clear()
            jsondb = (input('Insira o nome do seu arquivo: ').lower()).strip()

            # Check para ver se o arquivo já existe, para não deletar os dados que já estão nele
            # Ou criar uma outra lista, além da que já existe. usa a funçaõ exists(), do módulo path de os
            if path.exists(f'aula6/{jsondb}'):
                with open(f'aula6/{jsondb}.json', 'r', encoding='utf-8') as file:
                    old_data = json.load(file)

                # Método extend adiciona todos os elementos de uma lista ao fim de outra. 'append' adicionaria
                # apenas um elemento, e não todos os elementos separadamente.
                old_data.extend(users)

                # Abre o nosso json no formato certo, modo 'a', para adicionar ao arquivo ao invés de sobresvrever. nome dele no código é 'file'.
                with open(f'aula6/{jsondb}.json', 'a', encoding='utf-8') as file:

                    # Dump é uma função para salvar um arquivo em json. Parâmetros: users é o que vamos adicionar, old_data é onde vamos adicionar,
                    # ensure_ascii é falso para não dar erro em caracteres especiais, indent para separar no tanto de linhas necessário.

                    # Com mais clareza: users contém os dados novos que adicionamos, old_data são os dados antigos (se existirem) + os dados que adicionamos com extend
                    # Esse old_data sempre receberá o que foi escrito em users, e será transferido ao json.
                    json.dump(users, old_data, ensure_ascii=False, indent=0)
            
            else:
                with open(f'aula6/{jsondb}.json', 'w', encoding='utf-8') as file:
                    
                    json.dump(users, file, ensure_ascii=False, indent=1)
            

            print('Os dados foram adicionados ao JSON!')
            sleep(1)
            clear()
            continue

        case 3:
            clear()
            while True:
                try:
                    clear()
                    with open(f'aula6/{jsondb}.json', 'r', encoding='utf-8') as file:
                        
                        # Load carrega o arquivo json na variável dados, que agora é nosso dict
                        dados = json.load(file)
                    
                    print(f'{8 * '-'} Dados {8 * '-'}')

                    # Itera sobre cada dado presente no json (armazenado na lista, na var dados), e dentro dele itera sobre cada chave (uma para cada valor)
                    # json_dict = cada um dos dicionários dentro da lista de dicionários, que é 'dados'
                    # key = a chave de cada um dos dicionários

                    for json_dict in dados:
                        for key in json_dict:
                            print(f'{key} : {json_dict.get(key)}') # função get do dicionário recebe uma chave e retorna o valor correspondente.
                        
                        print('\n'f'{10 * '-'}''\n')

                    print('Exibição finalizada.')
                    sleep(10)
                    clear()
                    break
                
                # NameError é um erro levantado caso a variável 'jsondb' não seja encontrada.
                except NameError:
                    print('Erro. O arquivo não foi encontrado.''\n')
                    jsondb = (input('Insira o nome do seu arquivo: ').lower()).strip()

                    sleep(1)
                    continue

        case 4:
            clear()
            print('Já vai tarde.')
            break

        case _:
            clear()
            print('Valor inválido. Tente novamente.')
            sleep(1)
            continue


'''

    jsondb = (input('Insira o nome do seu arquivo: ').lower()).strip()
    with open(f'{jsondb}.txt', 'r', encodiing='utf-8'):

'''


