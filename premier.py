import math
import time
import unittest


def isprime(number: int) -> bool:
    for i in [x for x in range(2, int(number)) if (x == 2 or x % 2 == 1) and x <= math.sqrt(number)]:
        if i >= number:
            break
        elif number % i == 0:
            return False
    return True


def listePrime(max: int, resultat):
    for x in range(2, max):
        if isprime(x):
            resultat(x)


def noop(x: int):
    pass


def listePrimeSansAffichage(max: int):
    listePrime(max, noop)


def listePrimeAvecAffichage(max: int):
    print('liste de nombres premiers')
    listePrime(max, print)


def main():
    max: int = 100
    # max: int = 50000
    # max:int=100000

    calculTemps = True
    calculTemps = False

    if calculTemps:
        start = time.time()

        listePrimeSansAffichage(max)

        end = time.time()
        elapsed = end * 1000 - start * 1000

        print(f'Temps d\'exécution : {elapsed}ms')
    else:
        listePrimeAvecAffichage(max)


if __name__ == '__main__':
    main()


