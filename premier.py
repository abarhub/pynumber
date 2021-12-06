import math


def isprime(number: int) -> bool:
    for i in [x for x in range(2, int(number/2)) if (x==2 or x%2==1) and x<=math.sqrt(x)]:
        if i >= number:
            break
        elif number % i == 0:
            return False
    return True


def listePrime():
    print('liste de nombres premiers')
    for x in range(2, 50000):
        if isprime(x):
            print(x)



listePrime()
