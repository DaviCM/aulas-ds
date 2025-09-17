from time import sleep
from os import system

pw = input('Digite sua senha: ')
system('cls')
print('Informações sobre a senha:''\n')
print(f'Sua senha em letras maiúsculas é: {pw.upper()}')
print(f'Sua senha em letras minúsculas é: {pw.lower()}')
print(f'O tamanho dela é: {len(pw)} caracteres.')
print(f'Sua senha contém apenas números: {pw.isdigit()}')
