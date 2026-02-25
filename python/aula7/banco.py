from os import system
from time import sleep

users = {}

def pegarFloat(value):
    while True:
        try:
            retvalue = value
            retvalue = float((input(value).replace(',','.')).strip())
            
            if retvalue > 0:
                system('cls')
                return retvalue
            else:
                raise ValueError

        except ValueError:
            print('Valor inválido. Por favor, tente novamente.')
            sleep(1)
            system('cls')
            continue


def senha(value):
    while True:
        try:
            retvalue = value
            retvalue = input(retvalue).strip()
            
            if len(retvalue) == 6:
                system('cls')
                return retvalue
            else:
                raise ValueError

        except ValueError:
            print('Valor inválido. Por favor, tente novamente. (Senha)')
            sleep(1)
            system('cls')
            continue


def novaConta():
    while True:
        print('Hora de criar sua nova conta!')
        user = (input('Digite seu nome (Apenas caracteres do alfabeto são permitidos): ').title()).strip()
        
        # HACK HACK HACK Drible na função isalpha(), que não aceita espaços
        if (user in users.keys()) or ((user.replace(' ', '')).isalpha() == False):
            system('cls')
            print('Nome de usuário inválido. Insira outro.')
            sleep(2)
            system('cls')
            continue
        else:
            break
        
    pw = senha('Crie uma senha de seis números: ')
    saldo = 0.0

    print(f'Olá, {user}! Sua conta foi criada.')
    print(f'Seu saldo é de: R${saldo:.2f}.''\n')

    newuser = {user: [pw, saldo]}
    users.update(newuser)

    print(users)
    sleep(5)
    system('cls')


def acessarConta():
    while True:
        
        if users == {}:
            print('Não há contas para entrar. Cadastre uma conta antes.')
            sleep(2)
            system('cls')
            return False, None
        
        try:
            user = (input('Insira seu nome de usuário: ').title()).strip()
            pw = senha('Digite sua senha: ')

            if (user in users.keys()) and (pw in (users[user][0])):
                return True, user
            else:
                raise ValueError
        
        except ValueError:
            print('O usuário ou a senha estão errados. Tente novamente. (Acesso)')
            system('cls')
            sleep(2)
            continue


def gerirConta():
    valido, user = acessarConta()
    
    def sacar():
        while True:
            system('cls')
            print('1 - Sacar valor')
            
            if (users[user][1]) == 0:
                print('Você não possui saldo para sacar. Deposite um valor antes.')
                sleep(2)
                system('cls')
                break
            
            print(f'Esse é seu saldo: {(users[user][1]):.2f}')
            saque = pegarFloat('Insira o valor que deseja sacar: R$')
            
            if (saque > (users[user][1])) or (saque == 0):
                print('Operação Impossível. Você não possui esse valor.')
                print('Tente novamente.')
                sleep(2)
                system('cls')
                break
            else:
                (users[user][1]) -= saque
                print(f'Você sacou R${saque:.2f}.')
                print(f'Seu novo saldo é: R${(users[user][1]):.2f}.')
                sleep(2)
                system('cls')
                break

    
    def depositar():
        system('cls')
        print('2 - Depositar valor')
        depo = pegarFloat('Insira o valor que deseja depositar R$: ')

        (users[user][1]) += depo
        print(f'Você depositou R${depo:.2f}.')
        print(f'Seu novo saldo é: R${(users[user][1]):.2f}.')
        sleep(2)
        system('cls')
        
        
    def excluirConta():
        while True:
            system('cls')
            print('3 - Encerrar conta')
            
            if users[user][1] != 0:
                print('Você não pode deletar a conta, pois possui saldo nela. Faça o saque do valor para deletar.')
                sleep(2)
                system('cls')
                break
            
            del_acc = (input('Tem certeza que deseja seguir em frente? (n para voltar): ').lower()).strip()
            
            if del_acc == 'n':
                print('\n''Ufa, que bom!')
                sleep(1)
                system('cls')
                continue
            else:
                system('cls')
                pw = senha('Digite sua senha: ') 
                
                if pw in (users[user][0]):
                    print('Senha confirmada. Deletando conta.')
                    del users[user]
                    print(users)
                    print('Adeus, amigo.')
                    sleep(2)
                    system('cls')
                    break    
                else:
                    print('A senha inserida está errada. Tente novamente.')
                    continue
    
    
    while valido == True:
        print(f'Bem vindo à sua conta, {user}!')
        print(f'Você possui um saldo de: R${(users[user][1]):.2f}.''\n')
        print('1 - Sacar valor')
        print('2 - Depositar valor')
        print('3 - Encerrar conta')
        print('4 - Sair da conta''\n')
        cc_opt = input('Insira o que deseja fazer: ')

        match cc_opt:
            case '1':
                sacar()
                continue

            case '2':
                depositar()
                continue

            case '3':
                excluirConta()
                break
        
            case '4':
                system('cls')
                print('Saindo da sua conta.')
                sleep(1)
                system('cls')
                break

            case _:
                system('cls')
                print('Valor inválido. Por favor, tente novamente. (Conta Corrente)')
                sleep(1)
                system('cls')
                continue

    else:
        system('cls')


def main():
    system('cls')      
    while True:
        print(f'{5 * '-'} Bem Vindo ao Banco! {5 * '-'}')
        print('1 - Cadastrar novo usuário')
        print('2 - Acessar conta corrente')
        print('3 - Ir embora''\n')
        gn_opt = input('Insira o que deseja fazer: ')

        match gn_opt:
            case '1':
                system('cls')
                novaConta()
                continue

            case '2':
                system('cls')
                gerirConta()

            case '3':
                system('cls')
                print('Já vai tarde.')
                break

            case _:
                system('cls')
                print('Valor inválido. Por favor, tente novamente. (Geral)')
                sleep(1)
                system('cls')
                continue


main()


