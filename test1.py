import math
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

    def calcul(self, ordre: int) -> int:
        res: int = 0
        # for i in range(0, ordre + 1):
        # mult: Mult = self.liste[i]
        # for i in range(0, len(self.liste)):
        # mult: Mult = self.liste[i]
        for mult in self.liste:
            if mult.ordre <= ordre:
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


#                   A  B  C  D
#                         E  F
#                 =============
#                   AF BF CF DF
#                AE BE CE DE
#
#
#
#


def construit(numberList: list[str]) -> ListVariable:
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


def construitEquation(numberList: list[str], listeVariables: ListVariable) -> MultiplicationComplete:
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


def inList(liste: list[Variable], nom: str) -> bool:
    for x in liste:
        if x.nom == nom:
            return True
    return False


def getVariables(liste: list[Mult], nonAffecte: bool) -> list[Variable]:
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
            if not inList(list6, x.nom):
                list6.append(x)
    return list6


def incr(tab: list[int]) -> list[int]:
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


def listValue(n: int) -> list[list[int]]:
    res: list[list[int]] = []
    res2: list[int] = [0 for _ in range(0, n)]
    res.append(res2)

    res3: list[int] = res2.copy()
    while True:
        res3 = incr(res3)
        if len(res3) == 0:
            break
        else:
            res.append(res3)
    return res


def estValide(eq: MultiplicationComplete, ordre: int, exacte: bool = False) -> bool:
    res = eq.calcul(ordre)
    if res == -1:
        return False
    res2 = eq.valeur(ordre)
    if exacte:
        return res == res2
    else:
        return (res - res2) % (10 ** (ordre + 1)) == 0


def resolution2(eq: MultiplicationComplete, ordre: int, max: int) -> list[MultiplicationComplete]:
    listResultat: list[MultiplicationComplete] = []
    tmp = eq.getByOrder(ordre)
    print("ordre", str(ordre), str(tmp))

    listVariables: list[Variable] = getVariables(tmp, True)

    listValeur: list[list[int]] = listValue(len(listVariables))

    print("listVariables", str(listVariables))
    print("listValeur", str(listValeur))
    for val in listValeur:
        # affectation des valeurs
        for i in range(0, len(val)):
            v = listVariables[i]
            v.valeur = val[i]
        if estValide(eq, ordre, ordre + 1 >= max):
            if ordre + 1 < max:
                tmp2 = resolution2(eq, ordre + 1, max)
                listResultat.extend(tmp2)
            else:
                listResultat.append(eq.copy())
                print("eq", str(eq))
        for i in range(0, len(val)):
            v = listVariables[i]
            v.valeur = -1

    return listResultat


def calcul_resolution(nombre: str, affichage_resultat: bool) -> list[MultiplicationComplete]:
    list = [char for char in nombre]
    listeVariables: ListVariable = construit(list)

    print("var", str(listeVariables))

    eq = construitEquation(list, listeVariables)

    print("eq", str(eq))

    list2 = eq.getByOrder(0)

    print("list2", str(list2))

    print("ordre1", str(eq.getByOrder(1)))

    res: list[MultiplicationComplete] = []
    res = resolution2(eq, 0, len(eq.valeurs))

    if affichage_resultat:
        print('resultat:', str(res))
        i = 1
        for res2 in res:
            print('resultat ', str(i))
            listeVar: list[Variable] = getVariables(res2.liste, False)
            liste1: list[Variable] = [x for x in listeVar if x != None and x.nom.startswith('x')]
            liste2: list[Variable] = [x for x in listeVar if x != None and x.nom.startswith('y')]
            print('liste1:', str(liste1))
            print('liste2:', str(liste2))
            i += 1

    return res


def main():
    # n = '28741'
    # n = '21'
    n = '115'
    # n = '99400891'

    calcul_resolution(n, True)


if __name__ == '__main__':
    main()
