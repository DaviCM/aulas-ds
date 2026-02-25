operations = ['Insira seu nome: ', 'Insira sua idade: ', 'Insira seu ano de nascimento: ']
values = []

def PegarValores():
    for i in range (len(operations)):
        if 'nome' in operations[i]:
                a = input(operations[i]).strip()
                while a.isalpha() != True:
                    a = input('Por favor, insira apenas letras do alfabeto: ')
                values.append(a)
        else:
                a = input(operations[i]).strip()
                while a.isnumeric() != True:
                    a = input('Por favor, insira apenas números inteiros: ')
                values.append(a)
    return values


PegarValores()
print(values)
print(f'Seu nome é {values[0]}, você tem {values[1]} anos e nasceu em {values[2]}!')


'''
OBS: Dá pra criar uma lista de tuplas na função, para serem desempacotadas no 'for loop'. não sabia disso! 
A melhor forma de desenvolvimento com IA é pedindo pra ela fazer o código mais bonito e pythonico possível!
'''