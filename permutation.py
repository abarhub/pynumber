class Test1:
    def __init__(self):
        self.liste = []

    def containtSrc(self, n):
        for tmp in self.liste:
            if tmp[0] == n:
                return True
        return False

    def containtDest(self, n):
        for tmp in self.liste:
            if tmp[1] == n:
                return True
        return False

    def add(self, i, j):
        self.liste.append((i, j))

    def __str__(self):
        return self.liste.__str__()

    def __repr__(self):
        return self.__str__()


class Test2:
    def __init__(self):
        self.map = {}

    def containtSrc(self, n):
        return n in self.map

    def containtDest(self, n):
        return n in self.map.values()

    def add(self, i, j):
        self.map[i] = j

    def __str__(self):
        return self.map.__str__()

    def __repr__(self):
        return self.__str__()

    def clone(self):
        tmp = Test2()
        tmp.map = self.map.copy()


def test1():
    n = 4
    nb = 0
    liste1 = []
    for i in range(n + 1):
        for j in range(n + 1):
            if i != j:
                liste1.append((i, j))
                nb += 1
                print(i, "->", j)

    print("nb=", nb)

    liste2 = []
    for i in range((n + 1)):
        tmp = Test1()
        tmp.add(i, i + 1 % n)
        liste2.append(tmp)

    for i in range(3):
        for tmp in liste1:
            trouve = False
            for tmp2 in liste2:
                if not tmp2.containtSrc(tmp[0]) and not tmp2.containtDest(tmp[1]):
                    tmp2.add(tmp[0], tmp[1])
                    trouve = True
            if not trouve:
                tmp3 = Test1()
                tmp3.add(tmp[0], tmp[1])
                liste2.append(tmp3)

    print("liste2", liste2)
    print("liste2.size", len(liste2))


def ajouteSuite(test2, no, n, liste):
    if no <= n:
        premier = True
        for j in range(n + 1):
            if no != j:
                if premier:
                    tmp = test2
                    premier = False
                else:
                    tmp = Test2()
                    tmp.map = test2.map.copy()
                    liste.append(tmp)
                if n in tmp.map or j in tmp.map.values():
                    # on n'ajoute pas
                    pass
                else:
                    tmp.add(n, j)
                    ajouteSuite(tmp, no + 1, n, liste)


def test2():
    n = 4

    liste = []
    for i in range(n + 1):
        for j in range(n + 1):
            if i != j:
                tmp = Test2()
                tmp.add(i, j)
                liste.append(tmp)
                ajouteSuite(tmp, i + 1, n, liste)

    print("liste", liste)
    print("liste.size", len(liste))


def main():
    # test1()
    test2()


main()
