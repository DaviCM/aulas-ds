operations = ['Insira seu nome: ', 'Insira sua idade: ', 'Insira sua data de nascimento no formato DD/MM/AAAA: ']
values = []

for i in range(3):
    values.append(input(operations[i]).strip())
    if len(values) == 3:
        break
print(values)
    
while i == True:    
    try:
        values[1] = int(values[1])
        i == False
    except ValueError:
       values[2] = print('Esse valor para a idade não é inteiro. Insira outro: ')


print(f'Seu nome é {values[0]}, você tem {values[1]} anos e nasceu em {values[2]}!')


