import json
import time


def genere_solution():
    # a*x+b*y=c [10]

    resultat = []
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):

                tmp = {'a': a, 'b': b, 'c': c, 'result': []}
                resultat.append(tmp)
                for x in range(0, 10):
                    for y in range(0, 10):
                        if (a * x + b * y - c) % 10 == 0:
                            print(f'{a}*{x}+{b}*{y}={c}[10]')
                            tmp['result'].append({'x': x, 'y': y})

    return resultat


def main():
    with open('files/solution.json', "w") as f:
        start = time.time()

        res = genere_solution()

        end = time.time()
        elapsed = end * 1000 - start * 1000

        f.write(json.dumps(res, sort_keys=True, indent=4) + "\n")

        print(f'Temps d\'exécution : {elapsed}ms')


if __name__ == '__main__':
    main()
