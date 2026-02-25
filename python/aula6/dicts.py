from os import system

# Manipulação de dicts

user = {
    'nome': 'Miku',
    'idade': 18,
    'email': 'miku@mikumikudance.com',
    'peso': 39.56,
    'nascimento': '14/05/07'
}

system('cls')

for chave in user:
    print(f'{chave}: {user.get(chave)}')
    print(f'{type(user.get(chave))}')

users = ['cris', 'davi' ,'karython 60', 'nunes', 'senai']

# Ele nunca mostra o último elemento da 'range' de contagem.
print(users[0:4])

