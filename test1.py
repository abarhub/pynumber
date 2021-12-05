import math


class Variable:
    nom = ''
    valeur = -1

    def __init__(self, nom, valeur):
        self.nom = nom
        self.valeur = valeur

    def __str__(self):
        return self.val()

    def val(self):
        if self.valeur >= 0:
            return str(self.valeur)
        else:
            return self.nom

    def descr(self):
        return self.nom + '=' + str(self.valeur)


class Constante:
    valeur = 0

    def __init__(self, valeur):
        self.valeur = valeur

    def __str__(self):
        return str(self.valeur)


class ListVariable:
    liste = []

    def __str__(self):
        i = 0
        s = ''
        while i < len(self.liste):
            if i > 0:
                s += ','
            s += self.liste[i].nom + '=' + str(self.liste[i].valeur)
            i = i + 1
        return '[' + s + ']'

    def get(self, nom):
        for x in self.liste:
            if x.nom == nom:
                return x
        return None


class Mult:
    x = None
    y = None
    ordre = 0

    def __init__(self, x, y, ordre):
        self.x = x
        self.y = y
        self.ordre = ordre

    def __str__(self):
        return str(self.x) + '*' + str(self.y) + '(' + str(self.ordre) + ')'


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
    liste = []
    valeurs = []

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


#                   A  B  C  D
#                         E  F
#                 =============
#                   AF BF CF DF
#                AE BE CE DE
#
#
#
#


def construit(numberList):
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


def construitEquation(numberList, listeVariables):
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

n='28741'
#list = ['2', '8', '7', '4', '1']
list=[char for char in n]
listeVariables = construit(list)

print("var", str(listeVariables))

eq = construitEquation(list, listeVariables)

print("eq", str(eq))
