liste_premier = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print(f'premier:{liste_premier}')

z = complex(4, 3)
print(z)

i = complex(0, 1)

print(z ** i)

z = complex(4, 3)
print(z.real)
print(z.imag)

for i in range(10):
    print(i)

i = complex(0, 1)

for n in range(10):
    z = complex(4, 3 + n) ** (i + 2)
    print(f'{z * 20} {n} {z.imag % 20}')


def test_fonction1(liste, maximum=-1, range1=20, range2=3):
    if maximum == -1:
        maximum = max(liste) + 1
    pasTrouve = True
    nb = 0
    nbTrouve = 0
    for a1 in range(range1):
        for a2 in range(range1):
            for a3 in range(range2):
                for a4 in range(range2):
                    trouve = False
                    nb += 1
                    liste0 = []
                    print(f'parcourt ...')
                    for n in range(len(liste)):
                        if a1 == 0 and a2 == 0 and n == 0:
                            z = 0
                        else:
                            z = complex(a1, a2 + n) ** (complex(a4, a3))
                        val = int(z.imag % maximum)
                        print(f'{z * 20} {n} {z.imag % 5} {val}')
                        liste0 = liste0 + [val]
                    if liste == liste0:
                        trouve = True
                        pasTrouve = False
                        nbTrouve += 1
                        print(f"trouvé pour a1={a1} a2={a2} a3={a3}")
    print(f'liste: {liste}')
    print(f'range1: {range1}, range2: {range2}, max: {maximum}')
    print(f'nb tentative: {nb}')
    if pasTrouve:
        print("pas trouvé")
    else:
        print(f"trouvé: {nbTrouve}")


liste1 = [1, 2, 3, 4, 5]
liste1 = [1, 2, 4, 2, 1]
liste1 = [2, 3, 5, 7, 11]
# max = 5
# max = 6
# max = 12
# max = 20
maximum = -1

range1 = 20
range2 = 3
range1 = 50
range2 = 20

test_fonction1(liste1, maximum, range1, range2)
