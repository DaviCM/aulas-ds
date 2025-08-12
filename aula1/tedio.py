from time import sleep

n = 1

while True:
    print(f'O valor é: {n}')
    n += 1
    sleep(0.05)
    
    if '24' in str(n):
        print(f'{'-' * 5} Lá ele! {'-' * 5}')
        
