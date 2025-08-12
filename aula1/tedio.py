from time import sleep

n = 1

while True:
    print(f'O valor é: {n}')
    n += 1
    sleep(0.05)
    
    if '24' in str(n):
        print(f'Lá ele! O valor é {n}!')
        n += 1
        
