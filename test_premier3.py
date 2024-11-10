def contient_liste(liste, liste2):
    for liste3 in liste2:
        if liste3 == liste:
            return True
    return False


def test_fonction1(taille_liste, maximum, range1=20, range2=3):
    # pasTrouve = True
    nb = 0
    # nbTrouve = 0
    liste = []
    for a1 in range(range1):
        for a2 in range(range1):
            for a3 in range(range2):
                for a4 in range(range2):
                    # trouve = False
                    nb += 1
                    liste0 = []
                    print(f'parcourt ...')
                    for n in range(taille_liste):
                        if a1 == 0 and a2 == 0 and n == 0:
                            z = 0
                        else:
                            z = complex(a1, a2 + n) ** (complex(a4, a3))
                        val = int(z.imag % maximum)
                        # print(f'{z * 20} {n} {z.imag % 5} {val}')
                        liste0 = liste0 + [val]
                    if not contient_liste(liste0, liste):
                        # trouve = True
                        # pasTrouve = False
                        # nbTrouve += 1
                        # print(f"trouvé pour a1={a1} a2={a2} a3={a3}")
                        liste.append(liste0)
    print(f'taille_liste: {taille_liste}')
    print(f'range1: {range1}, range2: {range2}, max: {maximum}')
    print(f'nb elt: {len(liste)}')
    i = 0
    for liste4 in liste:
        print(f'{i}: {liste4}')
        i += 1

    liste_triee = sorted(liste, key=lambda x: (x[0], x[1], x[2], x[3], x[4]))
    print(f'liste trie:')
    i = 0
    for liste4 in liste_triee:
        print(f'{i}: {liste4}')
        i += 1


taille_liste = 5
maximum_element = 5

test_fonction1(taille_liste, maximum_element)
