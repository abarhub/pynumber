import itertools


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

    def complet(self, n, identity=False, cycle_court=False):
        for i in range(n + 1):
            if not self.containtSrc(n) or not self.containtDest(n):
                return False
            if not identity:
                if self.map[i] == i:
                    return False
            if not cycle_court:
                m = self.map[i]
                if m in self.map and self.map[m] == i:
                    return False
        return True


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
        for j in range(n + 1):
            tmp = Test2()
            tmp.map = test2.map.copy()
            if no in tmp.map or j in tmp.map.values():
                pass
            else:
                tmp.add(no, j)
                ajouteSuite(tmp, no + 1, n, liste)
    else:
        if test2.complet(n, False):
            liste.append(test2)


def list_permutation(n):
    liste = []
    n0 = 0
    for j in range(n + 1):
        tmp = Test2()
        tmp.add(n0, j)
        ajouteSuite(tmp, n0 + 1, n, liste)

    return liste


def test2():
    n = 4
    # n = 5
    # n = 8
    # n = 10

    liste = list_permutation(n)

    print("liste", liste)
    print("liste.size", len(liste))


def test3():
    n = 4
    liste_n = range(n + 1)
    list_elt = list(itertools.permutations(liste_n))
    print("liste", list_elt)
    print("liste.size", len(list_elt))


def test4():
    n = 4
    #n = 5
    # n = 8
    # n = 10

    liste = list_permutation(n)

    print("liste", liste)
    print("liste.size", len(liste))

    liste2 = liste.copy()
    n_max = n + 1
    max_val = (n_max) * 1
    min_val = 0
    min_val = -max_val
    nb_diff = 0
    # nb_diff = 1
    # nb_diff = 2

    res = [ele for ele in itertools.product(range(min_val, max_val), repeat=6)]

    for elt in res:
        liste3 = []
        for tmp in liste2:
            nbTrouve = 0
            liste_invalide = []
            for x in range(n_max):
                res = 0
                for i in range(len(elt)):
                    m = elt[i]
                    for j in range(i):
                        m = m * x
                    res += m
                if (res) % n_max == tmp.map[x]:
                    nbTrouve += 1
                else:
                    liste_invalide.append(str(x) + "->" + str(tmp.map[x]))
            if nbTrouve >= n - nb_diff + 1:
                print("trouve:", tmp, elt, nbTrouve, liste_invalide)
                pass
            else:
                liste3.append(tmp)
        liste2 = liste3

    # for i in range(max_val):
    #     for j in range(max_val):
    #         for k in range(max_val):
    #             for l in range(max_val):
    #                 liste3 = []
    #                 for tmp in liste2:
    #                     nbTrouve = 0
    #                     for x in range(n_max):
    #                         if (i * x + j + k * x * x + 0 * l * x * x * x) % n_max == tmp.map[x]:
    #                             nbTrouve += 1
    #                     if nbTrouve >= n:
    #                         pass
    #                     else:
    #                         liste3.append(tmp)
    #             liste2 = liste3

    print("liste2.size", len(liste2))


def main():
    # test1()
    # test2()
    # test3()
    test4()


main()
