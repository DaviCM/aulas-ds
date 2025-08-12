a = 'Karython'
b = 60
pi = 3.1415926535897932384626433
bool = False

print(f'{10*'-'} Bem vindo ao setor de curiosidades! {10*'-'}')

# Concatenações
# HORRIVEL: vírgula ou +
print('Meu nome é', a, 'e tenho', b, 'anos de idade!')

# CRIME DE GUERRA: .format
print('Meu nome é {} e tenho {} anos de idade!'.format(a, b))

# INCRIVEL: f-string (string formatada)
print(f'Meu nome é {a} e tenho {b} anos de idade!')

# Formatação de casas decimais
print(f'pi = {pi}')
print(f'pi = {pi:.2f}')


# Substituição de caracteres
num = input('Digite um valor decimal: ').replace(',' , '.')
num = float(num)
print(num)

# Atividades:
print(f'Tipo da variável {a}: {type(a)}')
print(f'Tipo da variável {b}: {type(b)}')
print(f'Tipo da variável {pi}: {type(pi)}')
print(f'Tipo da variável {bool}: {type(bool)}')

print(f'Curiosidade: 12 + 7 é igual a {12 + 7}')
print(f'Curiosidade: o resto da divisão 15 / 4 é {15 % 4}')
print(f'Curiosidade: 3 elevado ao quadrado é {3 ** 2}')

opa = input('Qual seu nome, meu nobre? ')
print(f'Seja bem vindo à programação em Java, {opa}!')

vinte = '20'
vinte = int(vinte)
print(f'{opa}, uma curiosidade pra você: 20 + 10 é: {vinte + 10}')



