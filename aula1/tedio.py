from time import sleep

n = 1

def LaEle():
    if '24' in str(n):
        print(f'Lá ele! O valor é {n}!')


while True:
    print(f'O valor é: {n}')
    LaEle()
    n += 1
    sleep(0.05)
    

    
