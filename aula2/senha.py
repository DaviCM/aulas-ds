from os import system

senha = input('Digite uma senha: ')
system('cls')
print(f'Sua senha é: {len(senha) * '*'}')
