from random import choice, randint

def funcA(rng=None):
    if rng == None:
        rng = randint(1, 10000)
    return rng

while True:
    print(funcA())


