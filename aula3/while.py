cont = 0
while cont < 10:
    cont += 1
    if cont % 2 == 0:
        print(cont)
    else:
        # Continue ignora o código restante na iteração, pulando para a seguinte.
        # Nesse caso, irá ignorar o print que restaria na iteração, voltando para o inicio do while.
        continue

    print('Contando...')
print('Cansei de contar.')



