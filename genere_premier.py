import math
import time


def isprime(number: int) -> bool:
    for i in [x for x in range(2, int(number)) if (x == 2 or x % 2 == 1) and x <= math.sqrt(number)]:
        if i >= number:
            break
        elif number % i == 0:
            return False
    return True


def listePrime(min:int ,max: int, resultat):
    for x in range(min, max):
        if isprime(x):
            resultat(x)


def noop(x: int):
    pass


def listePrimeSansAffichage(min:int,max: int, f):
    listePrime(min,max, lambda x: f.write(str(x)+"\n"))


def main():
    min=2
    #max: int = 100
    #max: int = 50000
    max:int=100000

    with open('files/primes_'+str(min)+'_'+str(max)+'.txt', "w") as f:


        start = time.time()

        listePrimeSansAffichage(min,max,f)

        end = time.time()
        elapsed = end * 1000 - start * 1000

        print(f'Temps d\'exécution : {elapsed}ms')



if __name__ == '__main__':
    main()
