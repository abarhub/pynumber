import copy
import logging
import random
import time

from factorisation import Resolution, ListValue, ListValueMemory, ListValueOptimise, MultiplicationComplete, \
    AbstractListValue


def test1():
    # n = '28741'
    # n = '21'
    # n = '115'
    n = '99400891'

    resolution = Resolution()
    listValue = ListValue()
    listValueMemory = ListValueMemory()
    listValueOptimise = ListValueOptimise()

    resolution.calcul_resolution(n, True, listValue.listValue)


def list_prime_number():
    file1 = open('files/primes_10_000_000.txt', 'r')
    Lines = file1.readlines()
    res = [int(x) for x in Lines]
    return res


def test2():
    logger = logging.getLogger(__name__)
    list = list_prime_number()
    list = [x for x in list if x > 10 and x < 10000]
    logger.info(f"primes: {list}")

    max = len(list)
    n01 = random.randint(0, max)
    n02 = random.randint(0, max)
    n1 = list[n01]
    n2 = list[n02]
    res = n1 * n2

    logger.info(f'n1={n1},n2={n2},res={res}')
    resolution = Resolution()
    listValue = ListValue()
    listValueMemory = ListValueMemory()
    listValueOptimise = ListValueOptimise()

    res2 = resolution.calcul_resolution(str(res), True, listValue.listValue)

    logger.info(f'result={res2}')


def test3():
    logger = logging.getLogger(__name__)
    list = list_prime_number()
    list = [x for x in list if x > 10 and x < 10000]
    logger.info(f"primes: {list}")

    max = len(list)
    nb = 10

    for i in range(10):
        n01 = random.randint(0, max)
        n02 = random.randint(0, max)
        n1 = list[n01]
        n2 = list[n02]
        res = n1 * n2

        logger.info(f'n1={n1},n2={n2},res={res}')
        resolution = Resolution()
        listValue = ListValue()
        # listValueMemory = ListValueMemory()
        # listValueOptimise = ListValueOptimise()

        res2 = resolution.calcul_resolution(str(res), True, listValue.listValue)

        logger.info(f'result={res2}')


class ListValue2(AbstractListValue):

    def __init__(self):
        self.map = {}
        self.listResultat = {}

    def incr(self, tab: list[int]) -> list[int]:
        len2 = len(tab)
        tab2: list[int] = tab.copy()
        pos = len2 - 1
        while pos >= 0:
            v = tab2[pos]
            if v < 9:
                v = v + 1
                tab2[pos] = v
                break
            else:
                tab2[pos] = 0
                pos = pos - 1
        if pos < 0:
            return []
        else:
            return tab2

    def listValue(self, n: int, ordre: int, eq: MultiplicationComplete, max: int) -> list[list[int]]:
        if n in self.map:
            return self.map[n]
        res: list[list[int]] = []
        res2: list[int] = [0 for _ in range(0, n)]
        res.append(res2)

        res3: list[int] = res2.copy()
        while True:
            res3 = self.incr(res3)
            if len(res3) == 0:
                break
            else:
                res.append(res3)
        self.map[n] = res
        return res

    def trouve(self, eq: MultiplicationComplete, ordre: int):
        if not eq.isNonFactorise():
            for o in range(ordre + 1):
                tmp = eq.getByOrder(o)
                for tmp2 in tmp:
                    tmp3 = (tmp2.x.valeur, tmp2.y.valeur, eq.valeurs)
                    if o not in self.listResultat:
                        self.listResultat[o] = []
                    self.listResultat[o].append(tmp3)


class ListValue3(AbstractListValue):

    def __init__(self, listeValue2: ListValue2):
        self.map = listeValue2.map
        self.listResultat = {}
        self.lastResult = listeValue2.listResultat
        self.dejaTrouve = False
        self.optimiseDejaTrouve = False

    def listValue(self, n: int, ordre: int, eq: MultiplicationComplete, max: int) -> list[list[int]]:
        if self.dejaTrouve:
            return []
        tmp = copy.deepcopy(self.map[n])
        if ordre in self.lastResult:
            tmp2 = self.lastResult[ordre]
            list2 = [[x[0], x[1]] for x in tmp2 if x[2] == eq.valeurs]
            list3 = []
            list4 = []
            for m in tmp:
                contient = False
                for g in list2:
                    if len(m) == 2 and len(g) == 2 and m[0] == g[0] and m[1] == g[1]:
                        contient = True
                if contient:
                    list3.append(m)
                else:
                    list4.append(m)
            tmp = []
            tmp.extend(list3)
            tmp.extend(list4)
        return tmp

    def trouve(self, eq: MultiplicationComplete, ordre: int):
        if self.optimiseDejaTrouve and not eq.isNonFactorise():
            self.dejaTrouve = True


def test4():
    logger = logging.getLogger(__name__)
    list = list_prime_number()
    list = [x for x in list if x > 10 and x < 10000]
    logger.info(f"primes: {list}")

    max = len(list)
    nb = 10

    listValue = ListValue2()
    entree = []

    start = time.time()

    for i in range(nb):
        n01 = random.randint(0, max)
        n02 = random.randint(0, max)
        n1 = list[n01]
        n2 = list[n02]
        res = n1 * n2
        entree.append((n1, n2, res))

        logger.info(f'n1={n1},n2={n2},res={res}')
        resolution = Resolution()
        # listValue = ListValue()
        # listValue = ListValue2()
        # listValueMemory = ListValueMemory()
        # listValueOptimise = ListValueOptimise()

        res2 = resolution.calcul_resolution(str(res), True, listValue)

        logger.info(f'result={res2}')

    end = time.time()
    elapsed = end * 1000 - start * 1000

    logger.info(f'listValue={listValue.listResultat}')

    logger.info(f'resolution2')

    listValue3 = ListValue3(listValue)

    listValue3.optimiseDejaTrouve = False
    listValue3.optimiseDejaTrouve = True

    start2 = time.time()

    for n in entree:
        listValue3.dejaTrouve = False

        n1, n2, res = n
        logger.info(f'n1={n1},n2={n2},res={res}')

        resolution = Resolution()

        res2 = resolution.calcul_resolution(str(res), True, listValue3)

        logger.info(f'result={res2}')

    end2 = time.time()
    elapsed2 = end2 * 1000 - start2 * 1000

    print(f'Temps d\'exécution (methode 1) : {elapsed}ms')
    print(f'Temps d\'exécution (methode 2) : {elapsed2}ms')


def main():
    # logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')
    # logging.basicConfig(level=logging.ERROR, format='%(levelname)s:%(message)s')

    # test1()
    # test2()
    # test3()
    test4()


if __name__ == '__main__':
    main()