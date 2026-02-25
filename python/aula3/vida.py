def vida():
    from random import randint
    from time import sleep

    morte = False
    dias_vivo = 1

    while morte == False:
        chance = randint(0,1000)
        if chance <= 995:
            print(f'Você sobreviveu ao dia {dias_vivo}.')
            dias_vivo += 1
            sleep(0.05)
        else:
            print(f'Você morreu hoje, dia {dias_vivo}. RIP.')
            morte = True

        if dias_vivo % 365 == 0:
            print('Você passou um ano vivo! Feliz aniversário!')


