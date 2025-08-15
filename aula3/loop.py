from os import system
from vida import vida

while True:
    print(f'{5*'-'} Bem vindo à TEORIA DE TUDO! {5*'-'}')

    print('1 - Seu IMC')
    print('2 - Maioridade')
    print('3 - Calculadora')
    print('4 - Dados pessoais')
    print('5 - Jogo da Vida')
    print('6 - Ir embora')
    opt = int(input('Escolha o que deseja saber hoje: '))

    if opt == 1:
        alt = float(input('Digite a sua altura: ').replace(',','.'))
        peso = float(input('Digite o seu peso: ').replace(',','.'))

        # Cálculo do IMC é sempre (peso) / (altura ao quadrado)
        imc = peso / (alt * alt)

        print('\n'f'Seu IMC é: {imc:.2f}.')

        # Valor tem que ser menor ou igual à condicional para entrar.
        # Se passar, irá para a próxima condicional.
        if imc <= 18.5:
            print('Abaixo do peso normal.')
        elif imc <= 24.9:
            print('Peso normal.')
        elif imc <= 29.9:
            print('Sobrepeso.')
        elif imc <= 34.9:
            print('Obesidade grau I.')
        elif imc <= 39.9:
            print('Obesidade grau II.')
        else:
            print('Obesidade grau III.')

    elif opt == 2:
        id = int(input('Digite a sua idade: '))
        print('Você é um adulto!' if id >= 18 else 'Vai embora, kid.')

    elif opt == 3:
        print('1 - Soma')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')

        opr = int(input('Escolha a operação que deseja realizar: '))
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))

        if opr == 1:
            print(f'Sua soma é: {n1 + n2}')
        elif opr == 2:
            print(f'Sua subtração: {n1 - n2}')
        elif opr == 3:
            print(f'Sua multiplicação é: {n1 * n2}')
        elif opr == 4:
            print(f'Sua divisão é: {n1 / n2}')
        else:
            print("Inválido. Reiniciando sistema.")
            pass

    elif opt == 4:
        print('Insira seus dados:')
        nome = input('Nome: ')
        id = input('Idade: ')
        cpf = input('CPF: ')
        tel = input('Telefone: ')

        print(f'Olá, {nome}! Vi que você tem {id} anos de idade e o CPF {cpf}!')
        print(f'Vou te ligar em {tel}!')

    elif opt == 5:
        vida()

    elif opt == 6:
        quit = True
    
    else:
        print('Inválido. Reiniciando sistema.')
        continue

    if quit == True:
        print('Já vai tarde.')
        break

    option = (input('Deseja continuar no programa? (s para continuar) ').lower()).strip()
    if option == 's':
        system('cls')
        continue

    else:
        print('Já vai tarde.')
        break


    
