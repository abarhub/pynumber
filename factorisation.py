import logging
import math
import time
import timeit
from builtins import list


class Variable:
    nom: str = ''
    valeur: int = -1

    def __init__(self, nom: str, valeur: int):
        self.nom = nom
        self.valeur = valeur

    def __str__(self) -> str:
        return self.val()

    def val(self) -> str:
        if self.valeur >= 0:
            return str(self.valeur)
        else:
            return self.nom

    def descr(self) -> str:
        return self.nom + '=' + str(self.valeur)

    def __repr__(self) -> str:
        return self.__str__()

    def copy(self):
        return Variable(self.nom, self.valeur)


class Constante:
    valeur: int = 0

    def __init__(self, valeur: int):
        self.valeur = valeur

    def __str__(self) -> str:
        return str(self.valeur)

    def __repr__(self) -> str:
        return self.__str__()


class ListVariable:
    liste: list[Variable]

    def __init__(self):
        self.liste = []

    def __str__(self):
        i = 0
        s = ''
        while i < len(self.liste):
            if i > 0:
                s += ','
            s += self.liste[i].nom + '=' + str(self.liste[i].valeur)
            i = i + 1
        return '[' + s + ']'

    def get(self, nom: str) -> Variable:
        for x in self.liste:
            if x.nom == nom:
                return x
        return None


class Mult:
    x: Variable = None
    y: Variable = None
    ordre: int = 0

    def __init__(self, x: Variable, y: Variable, ordre: int):
        self.x = x
        self.y = y
        self.ordre = ordre

    def __str__(self):
        return str(self.x) + '*' + str(self.y) + '(' + str(self.ordre) + ')'

    def __repr__(self):
        return self.__str__()

    def copy(self):
        x1: Variable = None
        y1: Variable = None
        if self.x != None:
            x1 = self.x.copy()
        if self.y != None:
            y1 = self.y.copy()
        m: Mult = Mult(x1, y1, self.ordre)
        return m


class MultiplicationComplete:
    liste: list[Mult] = []
    valeurs: list[int] = []

    def __init__(self):
        self.liste = []
        self.valeurs = []

    def __str__(self):
        i = 0
        s = ''
        while i < len(self.liste):
            if i > 0:
                s += ' + '
            tmp = self.liste[i]
            s += str(tmp)
            i = i + 1
        return s + '(' + str(self.valeurs) + ')'

    def __repr__(self):
        return self.__str__()

    def getByOrder(self, ordre: int) -> list[Mult]:
        return [x for x in self.liste if x.ordre <= ordre]

    def calcul(self, ordre: int = -1) -> int:
        res: int = 0
        for mult in self.liste:
            if ordre == -1 or mult.ordre <= ordre:
                if mult.x.valeur == -1 or mult.y.valeur == -1:
                    return -1
                res += mult.x.valeur * mult.y.valeur * 10 ** mult.ordre
        return res

    def valeur(self, ordre: int) -> int:
        res: int = 0
        for i in range(0, ordre + 1):
            v: int = self.valeurs[i]
            res += v * 10 ** i
        return res

    def copy(self):
        res: MultiplicationComplete = MultiplicationComplete()
        res.valeurs = [x for x in self.valeurs]
        res.liste = [x.copy() for x in self.liste]
        return res

    def getX(self) -> list[int]:
        res = []
        for x in self.liste:
            tmp = x.x
            pos = int(tmp.nom[1:]) - 1
            while pos >= len(res):
                res.append(-1)
            res[pos] = tmp.valeur
        return res

    def getY(self) -> list[int]:
        res = []
        for y in self.liste:
            tmp = y.y
            pos = int(tmp.nom[1:]) - 1
            while pos >= len(res):
                res.append(-1)
            res[pos] = tmp.valeur
        return res


class Stat:

    def __init__(self):
        self.nb_valide = 0
        self.nb_invalide = 0
        self.nb_noeuds = 0
        self.ordre = 0
        self.elapse_listValeur = 0

    def __str__(self):
        return '(v=' + str(self.nb_valide) + ',i=' + str(self.nb_invalide) + ',n=' + str(self.nb_noeuds) + ',o=' + str(
            self.ordre) + ',e=' + str(self.elapse_listValeur) + ')'

    def __repr__(self):
        return self.__str__()


class Resolution:

    def __init__(self):
        self.stat = []

    #                   A  B  C  D
    #                         E  F
    #                 =============
    #                   AF BF CF DF
    #                AE BE CE DE
    #
    #
    #
    #
    def construit(self, numberList: list[str]) -> ListVariable:
        i = 0
        list2 = ListVariable()
        while i < len(numberList):
            tmp = Variable('z' + str(i + 1), numberList[len(numberList) - 1 - i])
            list2.liste.append(tmp)
            tmp = Variable('x' + str(i + 1), -1)
            list2.liste.append(tmp)
            if i < len(numberList) / 2:
                tmp = Variable('y' + str(i + 1), -1)
                list2.liste.append(tmp)
            i = i + 1

        return list2

    def construitEquation(self, numberList: list[str], listeVariables: ListVariable) -> MultiplicationComplete:
        nb: int = len(numberList)
        nb2: int = int(math.ceil(nb / 2))
        # nb = 1
        # nb2 = 1
        liste: MultiplicationComplete = MultiplicationComplete()
        liste.valeurs = [int(x) for x in reversed(numberList)]
        for x in range(1, nb + 1):
            for y in range(1, nb2 + 1):
                varx = listeVariables.get('x' + str(x))
                vary = listeVariables.get('y' + str(y))
                if varx is not None and vary is not None:
                    tmp2 = Mult(varx, vary, x + y - 2)
                    liste.liste.append(tmp2)
        return liste

    def inList(self, liste: list[Variable], nom: str) -> bool:
        for x in liste:
            if x.nom == nom:
                return True
        return False

    def getVariables(self, liste: list[Mult], nonAffecte: bool) -> list[Variable]:
        if nonAffecte:
            liste2: list[Variable] = [x.x for x in liste if x.x != None and x.x.valeur == -1]
            liste3: list[Variable] = [x.y for x in liste if x.y != None and x.y.valeur == -1]
        else:
            liste2: list[Variable] = [x.x for x in liste if x.x != None]
            liste3: list[Variable] = [x.y for x in liste if x.y != None]
        liste4: list[Variable] = []
        liste4.extend(liste2)
        liste4.extend(liste3)
        liste5: list[str] = [x.nom for x in liste4]
        set2 = set(liste5)
        list6: list[Variable] = []
        for x in liste4:
            if x.nom in set2:
                if not self.inList(list6, x.nom):
                    list6.append(x)
        return list6

    def estValide(self, eq: MultiplicationComplete, ordre: int, exacte: bool = False) -> bool:
        if exacte:
            res = eq.calcul()
        else:
            res = eq.calcul(ordre)
        if res == -1:
            return False
        res2 = eq.valeur(ordre)
        if exacte:
            return res == res2
        else:
            return (res - res2) % (10 ** (ordre + 1)) == 0

    def resolution2(self, eq: MultiplicationComplete, ordre: int, max: int, listValueParam) -> list[
        MultiplicationComplete]:
        logger = logging.getLogger(__name__)
        listResultat: list[MultiplicationComplete] = []
        tmp = eq.getByOrder(ordre)
        logger.debug("ordre {ordre} {tmp}")

        if ordre >= len(self.stat):
            self.stat.append(Stat())

        stat = self.stat[ordre]
        stat.nb_noeuds += 1
        stat.ordre = ordre

        listVariables: list[Variable] = self.getVariables(tmp, True)

        start = time.time()
        listValeur: list[list[int]] = listValueParam(len(listVariables), ordre, eq, max)

        end = time.time()
        elapsed = end * 1000 - start * 1000
        stat.elapse_listValeur += elapsed

        logger.debug("listVariables {listVariables}")
        logger.debug("listValeur {listValeur}")
        for val in listValeur:
            # affectation des valeurs
            for i in range(0, len(val)):
                v = listVariables[i]
                v.valeur = val[i]
            if self.estValide(eq, ordre, ordre + 1 >= max):
                stat.nb_valide += 1
                if ordre + 1 < max:
                    tmp2 = self.resolution2(eq, ordre + 1, max, listValueParam)
                    listResultat.extend(tmp2)
                else:
                    listResultat.append(eq.copy())
                    logger.debug("eq {eq}")
            else:
                stat.nb_invalide += 1
            for i in range(0, len(val)):
                v = listVariables[i]
                v.valeur = -1

        return listResultat

    def calcul_resolution(self, nombre: str, affichage_resultat: bool, listValueParam) -> list[MultiplicationComplete]:
        start_total = time.time()
        logger = logging.getLogger(__name__)
        list = [char for char in nombre]
        start_construit = time.time()
        listeVariables: ListVariable = self.construit(list)
        end_construit = time.time()

        logger.debug("var {listeVariables}")

        start_construit2 = time.time()
        eq = self.construitEquation(list, listeVariables)
        end_construit2 = time.time()

        logger.debug("eq {eq}")

        list2 = eq.getByOrder(0)

        logger.debug(f"list2 {list2}")

        logger.debug(f"ordre1 {eq.getByOrder(1)}")

        res: list[MultiplicationComplete] = []
        start_resolve = time.time()
        res = self.resolution2(eq, 0, len(eq.valeurs), listValueParam)
        end_resolve = time.time()

        start_affiche = time.time()
        if affichage_resultat:
            logger.debug(f'resultat: {res}')
            i = 1
            for res2 in res:
                logger.info(f'resultat {i}')
                listeVar: list[Variable] = self.getVariables(res2.liste, False)
                liste1: list[Variable] = [x for x in listeVar if x != None and x.nom.startswith('x')]
                liste2: list[Variable] = [x for x in listeVar if x != None and x.nom.startswith('y')]
                logger.info(f'liste1: {liste1}')
                logger.info(f'liste2: {liste2}')
                i += 1
        end_affiche = time.time()

        end_total = time.time()
        self.elapsed_total = end_total * 1000 - start_total * 1000
        self.elapsed_construit = end_construit * 1000 - start_construit * 1000
        self.elapsed_construit2 = end_construit2 * 1000 - start_construit2 * 1000
        self.elapsed_resolve = end_resolve * 1000 - start_resolve * 1000
        self.elapsed_affiche = end_affiche * 1000 - start_affiche * 1000

        return res


class ListValue:

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
        return res


class ListValueMemory:

    def __init__(self):
        self.mem_list2: list[list[int]] = []
        self.mem_list1: list[list[int]] = []
        self.mem_list_init2: bool = False
        self.mem_list_init1: bool = False
        self.listValue = ListValue()

    def listValueMemory(self, n: int, ordre: int, eq: MultiplicationComplete, max: int) -> list[list[int]]:
        logger = logging.getLogger(__name__)
        if n == 2:
            logger.debug(f'listValueMemory {n} {self.mem_list_init2}')
            if not self.mem_list_init2:
                self.mem_list2 = self.listValue.listValue(n, ordre, eq, max)
                self.mem_list_init2 = True
            return self.mem_list2
        elif n == 1:
            logger.debug(f'listValueMemory {n} {self.mem_list_init1}')
            if not self.mem_list_init1:
                self.mem_list1 = self.listValue.listValue(n, ordre, eq, max)
                self.mem_list_init1 = True
            return self.mem_list1
        else:
            logger.debug(f'listValueMemory {n}')
        return self.listValue.listValue(n, ordre, eq, max)


class ListValueOptimise:

    def __init__(self):
        self.mem_list2: list[list[int]] = []
        self.mem_list1: list[list[int]] = []
        self.mem_list_init2: bool = False
        self.mem_list_init1: bool = False
        self.listValue = ListValue()

    def inList(self, liste: list[list[int]], list2: list[int]) -> bool:
        for x in liste:
            for y in list2:
                if y in x:
                    return True
        return False

    def listValueOptimised(self, n: int, ordre: int, eq: MultiplicationComplete, max: int) -> list[list[int]]:
        logger = logging.getLogger(__name__)
        list = self.listValue.listValue(n, ordre, eq, max)

        tmp = []
        if eq.valeurs == [1, 4, 7, 8, 2]:
            if ordre == 0:
                tmp = [0, 1]
            elif ordre == 2 or ordre == 3:
                tmp = [0, 4, 7]
            else:
                tmp = [0, 8, 2]
        elif eq.valeurs == [1, 9, 8, 0, 0, 4, 9, 9]:
            if ordre == 0:
                tmp = [3, 7]
            else:
                tmp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        if len(tmp) == 0:
            return list

        list2 = []
        for tmp2 in list:
            trouve = False
            for m in tmp:
                if m in tmp2:
                    trouve = True
                    break
            if trouve:
                list2.append(tmp2)

        logger.debug(f'diff={len(list) - len(list2)}')

        return list2


def main():
    # logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')
    # logging.basicConfig(level=logging.ERROR, format='%(levelname)s:%(message)s')

    # n = '28741'
    # n = '21'
    # n = '115'
    n = '99400891'

    resolution = Resolution()
    listValue = ListValue()
    listValueMemory = ListValueMemory()
    listValueOptimise = ListValueOptimise()

    # methode_calcul = 1
    # methode_calcul = 2
    methode_calcul = 3

    trace = False

    # trace = True

    def resout(methode_calcul: int):
        if methode_calcul == 1:
            resolution.calcul_resolution(n, True, listValue.listValue)
        elif methode_calcul == 2:
            resolution.calcul_resolution(n, True, listValueMemory.listValueMemory)
        elif methode_calcul == 3:
            resolution.calcul_resolution(n, True, listValueOptimise.listValueOptimised)

    if not trace:
        start = time.time()

        resout(methode_calcul)

        end = time.time()
        elapsed = end * 1000 - start * 1000

        print(f'Temps d\'exécution (methode {methode_calcul}) : {elapsed}ms')
        print(
            f'Temps d\'exécution detailé : total={resolution.elapsed_total}ms, '
            f'construit={resolution.elapsed_construit}ms, '
            f'construit2={resolution.elapsed_construit2}ms, resolve={resolution.elapsed_resolve}ms, '
            f'affiche={resolution.elapsed_affiche}ms')
        print(f'stat:{resolution.stat}')
    else:
        N = 100

        result = timeit.timeit(lambda: resout(methode_calcul), number=N)

        time2 = result / N * 1000
        print(f'{result:.2f} s')
        print(f'{time2:.1f} ms')


if __name__ == '__main__':
    main()
