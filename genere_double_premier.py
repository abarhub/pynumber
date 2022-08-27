import math
import time
from typing import TextIO


def isprime(number: int) -> bool:
    for i in [x for x in range(2, int(number)) if (x == 2 or x % 2 == 1) and x <= math.sqrt(number)]:
        if i >= number:
            break
        elif number % i == 0:
            return False
    return True


def listePrime(min: int, max: int, resultat):
    for x in range(min, max):
        if isprime(x):
            resultat(x)


def genere_double_premier(min: int, max: int, nb_chiffre: int, f: TextIO):
    list_prime = []
    listePrime(min, max, lambda x: list_prime.append(x))

    min0 = 10 ** (nb_chiffre - 1)
    max0 = 10 ** (nb_chiffre) - 1

    for i in range(min0, max0):
        if i > 2 and i % 2 == 0:
            continue
        for x in list_prime:
            if i % x == 0:
                n = i / x
                for y in list_prime:
                    if y <= x and n % y == 0:
                        m = n / y
                        if m == 1:
                            print(str(x), '*', str(y), '=', str(i))
                            f.write(str(x) + '*' + str(y) + '=' + str(i) + '\n')


def main():
    # nb_chiffre = 2
    # nb_chiffre = 5
    nb_chiffre = 10

    min = 2
    max: int = 10 ** nb_chiffre - 1

    with open('files/double_primes_' + str(nb_chiffre) + '.txt', "w") as f:
        start = time.time()

        genere_double_premier(min, max, nb_chiffre, f)

        end = time.time()
        elapsed = end * 1000 - start * 1000

        print(f'Temps d\'exécution : {elapsed}ms')


if __name__ == '__main__':
    main()
