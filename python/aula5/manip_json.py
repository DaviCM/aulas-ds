import json

try:
    newjson = (input('insira o nome do seu arquivo: ').lower()).strip()

    with open(f'{newjson}.json', 'r', encoding='utf-8') as file:
        # load() éa função que carrega um json.
        dados = json.load(file)

    print(f'{8 * '-'} Dados {8 * '-'}')

    # Itera sobre o conjunto de dados que nós temos (que no caso é a estrutura json), pegando cada dado individualmente.
    for dado in dados:
        # Itera sobre cada um dos lados, pegando sua chave.
        for chave in dado:
            print(f'{chave.capitalize()} : {dado.get(chave)}')
        
        print('\n'f'{10 * '-'}''\n')

except Exception as e:
    print(f'Não foi possível ler o arquivo. Erro: {e}')


