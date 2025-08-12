from time import sleep

n = 1

while True:
    n += 1
    
    print(f'O valor é: {n}')
    sleep(0.05)
    
    if '24' in str(n):
        print(f'{'-' * 15} Lá ele! {"-" * 15}')

