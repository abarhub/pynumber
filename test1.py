import math
from builtins import list


class Variable:
    nom: str = ''
    valeur:int = -1

    def __init__(self, nom:str, valeur:int):
        self.nom = nom
        self.valeur = valeur

    def __str__(self)->str:
        return self.val()

    def val(self)->str:
        if self.valeur >= 0:
            return str(self.valeur)
        else:
            return self.nom

    def descr(self)->str:
        return self.nom + '=' + str(self.valeur)

    def __repr__(self)->str:
        return self.__str__()


class Constante:
    valeur:int = 0

    def __init__(self, valeur:int):
        self.valeur = valeur

    def __str__(self)->str:
        return str(self.valeur)

    def __repr__(self)->str:
        return self.__str__()


class ListVariable:
    liste:list[Variable] = []

    def __str__(self):
        i = 0
        s = ''
        while i < len(self.liste):
            if i > 0:
                s += ','
            s += self.liste[i].nom + '=' + str(self.liste[i].valeur)
            i = i + 1
        return '[' + s + ']'

    def get(self, nom:str)->Variable:
        for x in self.liste:
            if x.nom == nom:
                return x
        return None


class Mult:
    x = None
    y = None
    ordre:int = 0

    def __init__(self, x, y, ordre:int):
        self.x = x
        self.y = y
        self.ordre = ordre

    def __str__(self):
        return str(self.x) + '*' + str(self.y) + '(' + str(self.ordre) + ')'

    def __repr__(self):
        return self.__str__()

# class Equation:
#     list = []
#     valeur = 0
#
#     def __str__(self):
#         i = 0
#         s = ''
#         while i < len(self.list):
#             if i > 0:
#                 s += ' + '
#             tmp = self.list[i]
#             s += str(tmp)
#             i = i + 1
#         return s


class MultiplicationComplete:
    liste:list[Mult] = []
    valeurs:list[int] = []

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

    def getByOrder(self,ordre:int)->list[Mult]:
        return [x for x in self.liste if x.ordre<=ordre]

#                   A  B  C  D
#                         E  F
#                 =============
#                   AF BF CF DF
#                AE BE CE DE
#
#
#
#


def construit(numberList:list[str])->ListVariable:
    i = 0
    list = ListVariable()
    while i < len(numberList):
        tmp = Variable('z' + str(i + 1), numberList[len(numberList) - 1 - i])
        list.liste.append(tmp)
        tmp = Variable('x' + str(i + 1), -1)
        list.liste.append(tmp)
        if i < len(numberList) / 2:
            tmp = Variable('y' + str(i + 1), -1)
            list.liste.append(tmp)
        i = i + 1

    # list=['z'+str(x+1) for x in range(len(numberList))]
    return list


def construitEquation(numberList :list[str], listeVariables: list)-> MultiplicationComplete:
    nb = len(numberList)
    nb2 = int(math.ceil(nb / 2))
    # nb = 1
    # nb2 = 1
    liste = MultiplicationComplete()
    liste.valeurs = [int(x) for x in reversed(numberList)]
    for x in range(1, nb2):
        for y in range(1, nb):
            varx = listeVariables.get('x' + str(x))
            vary = listeVariables.get('y' + str(y))
            if varx is not None and vary is not None:
                # tmp = Equation()
                # liste.liste.append(tmp)
                tmp2 = Mult(varx, vary, x + y - 2)
                # tmp.list.append(tmp2)
                liste.liste.append(tmp2)
    return liste

def inList(liste:list[Variable], nom:str)-> bool:
    for x in liste:
        if x.nom==nom:
            return True
    return False

def getVariables(liste:list[Mult])->list[Variable]:
    liste2:list[Variable]=[x.x for x in liste if x.x!=None and x.x.valeur>=0]
    liste3:list[Variable] = [x.y for x in liste if x.y != None and x.y.valeur>=0]
    liste4:list[Variable]=[]
    liste4.append(liste2)
    liste4.append(liste3)
    liste5:list[str]=[x.nom for x in liste4]
    set=set(liste5)
    list6:list[Variable]=[]
    for x in liste4:
        if x.nom in set:
            if not inList(list6,x.nom):
                list6.append(x)
    return list6


def resolution(eq:MultiplicationComplete):
    for i in range(0, int(math.ceil(len(eq.valeurs) / 2))):
        tmp = eq.getByOrder(i)
        print("ordre", str(i), str(tmp))

        listVariables=getVariables(tmp)
        for x in range(0, 10):
            for y in range(0, 10):
                # renseiger les variables
                pass

n='28741'
#list = ['2', '8', '7', '4', '1']
list=[char for char in n]
listeVariables = construit(list)

print("var", str(listeVariables))

eq = construitEquation(list, listeVariables)

print("eq", str(eq))

list2=eq.getByOrder(0)

print("list2", str(list2))

print("ordre1", str(eq.getByOrder(1)))


resolution(eq)



