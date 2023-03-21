import copy
import json
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


class ListValue4(ListValue2):

    def __init__(self):
        ListValue2.__init__(self)
        self.valsPossibleMax = {}
        self.valsPossibleMin = {}
        self.valsPossibleNb = {}

    def valeurPossibles(self, ordre: int, list: list[list[int]]):
        n = len(list)
        if ordre not in self.valsPossibleMax:
            self.valsPossibleMax[ordre] = n
        else:
            self.valsPossibleMax[ordre] = max(n, self.valsPossibleMax[ordre])
        if ordre not in self.valsPossibleMin:
            self.valsPossibleMin[ordre] = n
        else:
            self.valsPossibleMin[ordre] = min(n, self.valsPossibleMin[ordre])
        if ordre not in self.valsPossibleNb:
            self.valsPossibleNb[ordre] = 1
        else:
            self.valsPossibleNb[ordre] = self.valsPossibleNb[ordre] + 1

    def entre(self, ordre: int, val: list[int]):
        pass

    def sort(self, ordre: int, val: list[int]):
        pass

    def valeurTrouve(self, ordre: int, val: list[int]):
        pass


def test5():
    logger = logging.getLogger(__name__)

    # n = '28741'
    # n = '21'
    # n = '115'
    n = '99400891'

    resolution = Resolution()
    # listValue = ListValue()
    listValue = ListValue4()
    # listValueMemory = ListValueMemory()
    # listValueOptimise = ListValueOptimise()

    resolution.calcul_resolution(n, True, listValue)

    print(f"valsPossibleMax={listValue.valsPossibleMax}")
    print(f"valsPossibleMin={listValue.valsPossibleMin}")
    print(f"valsPossibleNb={listValue.valsPossibleNb}")


class ListValue5(ListValue2):

    def __init__(self):
        ListValue2.__init__(self)
        self.valsPossibleMax = {}
        self.valsPossibleMin = {}
        self.valsPossibleNb = {}
        self.pileValeurs = []
        self.text = ""

    def valeurPossibles(self, ordre: int, list: list[list[int]]):
        n = len(list)
        if ordre not in self.valsPossibleMax:
            self.valsPossibleMax[ordre] = n
        else:
            self.valsPossibleMax[ordre] = max(n, self.valsPossibleMax[ordre])
        if ordre not in self.valsPossibleMin:
            self.valsPossibleMin[ordre] = n
        else:
            self.valsPossibleMin[ordre] = min(n, self.valsPossibleMin[ordre])
        if ordre not in self.valsPossibleNb:
            self.valsPossibleNb[ordre] = 1
        else:
            self.valsPossibleNb[ordre] = self.valsPossibleNb[ordre] + 1

    def entre(self, ordre: int, val: list[int]):

        if len(val) > 0:
            n = ""
            if len(self.pileValeurs) > 0:
                val0 = self.pileValeurs[-1]
                if len(val0) > 0:
                    n += "x" + str(ordre - 1) + "_" + str(val0[0])
                    if len(val0) > 1:
                        n += "y" + str(ordre - 1) + "_" + str(val0[1])
            else:
                n += "xy"
            n += " -> "
            n += "x" + str(ordre) + "_" + str(val[0])
            if len(val) > 1:
                n += "y" + str(ordre) + "_" + str(val[1])
            self.text += "\n" + n
        self.pileValeurs.append(val)

    def sort(self, ordre: int, val: list[int]):
        self.pileValeurs.pop(-1)

    def valeurTrouve(self, ordre: int, val: list[int]):
        pass


def test6():
    logger = logging.getLogger(__name__)

    n = '28741'
    # n = '21'
    # n = '115'
    # n = '99400891'

    resolution = Resolution()
    # listValue = ListValue()
    listValue = ListValue5()
    # listValueMemory = ListValueMemory()
    # listValueOptimise = ListValueOptimise()

    resolution.calcul_resolution(n, True, listValue)

    print(f"valsPossibleMax={listValue.valsPossibleMax}")
    print(f"valsPossibleMin={listValue.valsPossibleMin}")
    print(f"valsPossibleNb={listValue.valsPossibleNb}")
    # print(f"text={listValue.text}")
    text_file = open("files/number.dot", "w")
    text_file.write('digraph {\n' + listValue.text + '\n}')
    text_file.close()

    # generer le svg avec la commande
    # dot -Tsvg number.dot >res.svg


class ListValue6(ListValue2):

    def __init__(self):
        ListValue2.__init__(self)
        self.valsPossibleMax = {}
        self.valsPossibleMin = {}
        self.valsPossibleNb = {}
        self.pileValeurs = []
        self.text = ""
        self.rootNode = ""
        self.eq = None
        self.listNodes = []
        self.lastNo = 1
        self.rootNo = 0

    def valeurPossibles(self, ordre: int, list: list[list[int]]):
        n = len(list)
        if ordre not in self.valsPossibleMax:
            self.valsPossibleMax[ordre] = n
        else:
            self.valsPossibleMax[ordre] = max(n, self.valsPossibleMax[ordre])
        if ordre not in self.valsPossibleMin:
            self.valsPossibleMin[ordre] = n
        else:
            self.valsPossibleMin[ordre] = min(n, self.valsPossibleMin[ordre])
        if ordre not in self.valsPossibleNb:
            self.valsPossibleNb[ordre] = 1
        else:
            self.valsPossibleNb[ordre] = self.valsPossibleNb[ordre] + 1

    def entre(self, ordre: int, val: list[int]):

        if len(val) > 0:
            n = self.getName(val, ordre)
            no = self.lastNo
            self.lastNo = self.lastNo + 1
            attr = self.getAttr(val, ordre, no, False)
            o = {"valeurs": val, "label": n, "no": no}
            n2 = ""
            if n not in self.listNodes:
                n2 += "\nCREATE (" + n + ":Soluce " \
                                         "{" + attr + "});"
                self.listNodes.append(n)

            n3 = ""
            if len(self.pileValeurs) > 0:
                o0 = self.pileValeurs[-1]
                n3 = o0["label"]
            else:
                n3 += self.rootNode

            if len(n3) > 0:
                n2 += "\n" + "CREATE (" + n3 + ")-[:SOL]->(" + n + ");"

            self.text += n2
            self.pileValeurs.append(o)

    def sort(self, ordre: int, val: list[int]):
        self.pileValeurs.pop(-1)

    def valeurTrouve(self, ordre: int, val: list[int]):
        v = self.pileValeurs[-1]
        n = "\nMATCH (s:Soluce {no: " + str(v["no"]) + "}) SET s.estSolution = true;"
        self.text += n

    def getName(self, val, ordre):
        n = "x" + str(ordre) + "_" + str(val[0])
        if len(val) > 1:
            n += "_y" + str(ordre) + "_" + str(val[1])
        return n

    def getAttr(self, val: list[int], ordre: int, no: int, racine: bool):
        attr = "x:" + str(val[0])
        if len(val) > 1:
            attr += ",y:" + str(val[1])
        attr += ",ordre:" + str(ordre)
        attr += ",racine:" + str(racine)
        attr += ",estSolution:false"
        attr += ",no:" + str(no)
        if racine:
            n = "R"
        else:
            n = str(val[0]) + "*x" + str(ordre)
            if len(val) > 1:
                n += "+" + str(val[1]) + "*y" + str(ordre)
        attr += ",text:\"" + n + "\""
        return attr

    def listValue(self, n: int, ordre: int, eq: MultiplicationComplete, max: int) -> list[list[int]]:
        res = super().listValue(n, ordre, eq, max)
        if self.eq == None:
            self.eq = eq
            self.rootNode = "rootxy"
            self.rootNo = self.lastNo
            self.lastNo += 1
            attr = self.getAttr([0, 0], -1, self.rootNo, True)
            self.text += "\nCREATE (" + self.rootNode + ":Soluce " \
                                                        "{" + attr + "});\n"

            i = 0
            lastNode = ""
            for v in eq.valeurs:
                node = "res" + str(i)
                self.text += "\nCREATE (" + node + ":Valeur " \
                                                   "{val:" + str(v) + ",ordre:" + str(i) + "})"

                if len(lastNode) > 0:
                    parent = lastNode
                else:
                    parent = self.rootNode
                self.text += "\n" + "CREATE (" + parent + ")-[:VAL]->(" + node + ")"

                lastNode = node
                i += 1

            self.text += "\n"

        return res


def test7():
    logger = logging.getLogger(__name__)

    # n = '28741'
    # n = '21'
    n = '115'
    # n = '99400891'

    resolution = Resolution()
    # listValue = ListValue()
    listValue = ListValue6()
    # listValueMemory = ListValueMemory()
    # listValueOptimise = ListValueOptimise()

    resolution.calcul_resolution(n, True, listValue)

    print(f"valsPossibleMax={listValue.valsPossibleMax}")
    print(f"valsPossibleMin={listValue.valsPossibleMin}")
    print(f"valsPossibleNb={listValue.valsPossibleNb}")
    # print(f"text={listValue.text}")
    text_file = open("files/neo4j_numb.txt", "w")
    text_file.write('// MATCH (n:Valeur) DETACH DELETE n\n' +
                    '// MATCH (n:Soluce) DETACH DELETE n\n' +
                    listValue.text + '\n')
    text_file.close()

    # generer le svg avec la commande
    # dot -Tsvg number.dot >res.svg


class ListValue8(ListValue2):

    def __init__(self):
        ListValue2.__init__(self)
        self.valsPossibleMax = {}
        self.valsPossibleMin = {}
        self.valsPossibleNb = {}
        self.pileValeurs = []
        self.text = ""
        self.rootNode = ""
        self.eq = None
        self.listNodes = []
        self.lastNo = 1
        self.rootNo = 0

    def valeurPossibles(self, ordre: int, list: list[list[int]]):
        n = len(list)
        if ordre not in self.valsPossibleMax:
            self.valsPossibleMax[ordre] = n
        else:
            self.valsPossibleMax[ordre] = max(n, self.valsPossibleMax[ordre])
        if ordre not in self.valsPossibleMin:
            self.valsPossibleMin[ordre] = n
        else:
            self.valsPossibleMin[ordre] = min(n, self.valsPossibleMin[ordre])
        if ordre not in self.valsPossibleNb:
            self.valsPossibleNb[ordre] = 1
        else:
            self.valsPossibleNb[ordre] = self.valsPossibleNb[ordre] + 1

    def entre(self, ordre: int, val: list[int]):

        if len(val) > 0:
            n = self.getName(val, ordre)
            no = self.lastNo
            self.lastNo = self.lastNo + 1
            attr = self.getAttr(val, ordre, no, False)
            o = {"valeurs": val, "label": n, "no": no}
            n2 = ""
            if n not in self.listNodes:
                # n2 += "\nCREATE (" + n + ":Soluce " \
                #                         "{" + attr + "});"
                self.listNodes.append(n)

            n3 = ""
            if len(self.pileValeurs) > 0:
                o0 = self.pileValeurs[-1]
                n3 = o0["label"]
            else:
                n3 += self.rootNode

            n1_name = "x" + str(ordre)
            n1_val = val[0]

            tmp_var = {
                n1_name: n1_val
            }
            if len(val) > 1:
                n2_name = "y" + str(ordre)
                n2_val = val[1]
                tmp_var[n2_name] = n2_val

            tmp0 = {
                "action": "entre",
                "ordre": ordre,
                "valeurs": val,
                "var": tmp_var,
                "eq": str(self.eq)
            }

            if len(n3) > 0:
                n2 += json.dumps(tmp0) + "\n"

            self.text += n2
            self.pileValeurs.append(o)

    def sort(self, ordre: int, val: list[int]):
        self.pileValeurs.pop(-1)
        tmp0 = {
            "action": "sort",
            "ordre": ordre,
            "valeurs": val
        }
        self.text += json.dumps(tmp0) + "\n"

    def valeurTrouve(self, ordre: int, val: list[int]):
        v = self.pileValeurs[-1]
        # n = "\nMATCH (s:Soluce {no: " + str(v["no"]) + "}) SET s.estSolution = true;"
        # self.text += n
        tmp0 = {
            "action": "trouve",
            "ordre": ordre,
            "valeurs": val,
            "resultat": str(v["no"]),
            "solution": True,
            "eq": str(self.eq)
        }
        self.text += json.dumps(tmp0) + "\n"

    def getName(self, val, ordre):
        n = "x" + str(ordre) + "_" + str(val[0])
        if len(val) > 1:
            n += "_y" + str(ordre) + "_" + str(val[1])
        return n

    def getAttr(self, val: list[int], ordre: int, no: int, racine: bool):
        attr = "x:" + str(val[0])
        if len(val) > 1:
            attr += ",y:" + str(val[1])
        attr += ",ordre:" + str(ordre)
        attr += ",racine:" + str(racine)
        attr += ",estSolution:false"
        attr += ",no:" + str(no)
        if racine:
            n = "R"
        else:
            n = str(val[0]) + "*x" + str(ordre)
            if len(val) > 1:
                n += "+" + str(val[1]) + "*y" + str(ordre)
        attr += ",text:\"" + n + "\""
        return attr

    def listValue(self, n: int, ordre: int, eq: MultiplicationComplete, max: int) -> list[list[int]]:
        res = super().listValue(n, ordre, eq, max)
        if self.eq == None:
            self.eq = eq
            self.rootNode = "rootxy"
            self.rootNo = self.lastNo
            self.lastNo += 1
            attr = self.getAttr([0, 0], -1, self.rootNo, True)
            # self.text += "\nCREATE (" + self.rootNode + ":Soluce " \
            #                                             "{" + attr + "});\n"

            i = 0
            lastNode = ""
            for v in eq.valeurs:
                node = "res" + str(i)
                # self.text += "\nCREATE (" + node + ":Valeur " \
                #                                    "{val:" + str(v) + ",ordre:" + str(i) + "})"

                if len(lastNode) > 0:
                    parent = lastNode
                else:
                    parent = self.rootNode
                # self.text += "\n" + "CREATE (" + parent + ")-[:VAL]->(" + node + ")"

                lastNode = node
                i += 1

            # self.text += "\n"

        return res


def test8():
    logger = logging.getLogger(__name__)

    # n = '28741'
    # n = '21'
    n = '115'
    # n = '99400891'

    resolution = Resolution()
    # listValue = ListValue()
    listValue = ListValue8()
    # listValueMemory = ListValueMemory()
    # listValueOptimise = ListValueOptimise()

    resolution.calcul_resolution(n, True, listValue)

    print(f"valsPossibleMax={listValue.valsPossibleMax}")
    print(f"valsPossibleMin={listValue.valsPossibleMin}")
    print(f"valsPossibleNb={listValue.valsPossibleNb}")
    # print(f"text={listValue.text}")
    text_file = open(f"files/trace_{n}.txt", "w")
    text_file.write(  # '// MATCH (n:Valeur) DETACH DELETE n\n' +
        # '// MATCH (n:Soluce) DETACH DELETE n\n' +
        listValue.text + '\n')
    text_file.close()

    # generer le svg avec la commande
    # dot -Tsvg number.dot >res.svg


def main():
    # logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')
    # logging.basicConfig(level=logging.ERROR, format='%(levelname)s:%(message)s')

    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    test8()


if __name__ == '__main__':
    main()
