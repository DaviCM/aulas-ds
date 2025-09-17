from time import sleep
from os import system

vens = []
counter = 1

system('cls')
print('Bem vindo ao gerenciador de vendas!''\n')
    
while True:
    ven = input(f'Insira o valor da {counter}º venda (enter para parar) R$: ').replace(',', '.')
    
    if ven.isdigit() == True:
        system('cls')
        vens.append(float(ven.strip()))
        counter += 1
    elif ven == '' and vens != []:
        system('cls')
        print('Resultados: ''\n')
        print(f'Total de vendas: {len(vens)}')
        print(f'Montante total de vendas: R${sum(vens):.2f}')
        print(f'Maior venda: R${max(vens):.2f}')
        print(f'Menor venda: R${min(vens):.2f}')
        print(f'Média aritmética das vendas: R${(sum(vens) / len(vens)):.2f}')
        break
    else:
        system('cls')
        print('Valor inválido. Tente novamente.')
        sleep(1)
        system('cls')
        continue
        

