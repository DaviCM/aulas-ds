from os import system

# Abrindo um arquivo, lendo e escrevendo para ele
# Chama o arquivo com o operador with, passa o nome do arquivo como parâmetro e 'r' para indicar que será feita leitura (read)
# Encoding é utf-8, o padrão de codificação de caracteres ascii

with open('texto.txt', 'r', encoding='utf-8') as file:
    texto = file.read()

system('cls')
print(texto, '\n')


