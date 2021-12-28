import unittest

from test1 import ListVariable, construit, construitEquation, MultiplicationComplete, resolution2, calcul_resolution, \
    Mult, Variable, getVariables


class MyTestCase(unittest.TestCase):

    def checkVarDefine(self, listeVariables: ListVariable, name: str, value: any) -> None:
        x = listeVariables.get(name)
        self.assertNotEqual(None, x)
        self.assertEqual(value, x.valeur)

    def test_construit(self):
        tab = ['1', '2', '3']
        listeVariables: ListVariable = construit(tab)
        self.assertEqual(8, len(listeVariables.liste))
        self.checkVarDefine(listeVariables, 'x1', -1)
        self.checkVarDefine(listeVariables, 'x2', -1)
        self.checkVarDefine(listeVariables, 'x3', -1)
        self.checkVarDefine(listeVariables, 'y1', -1)
        self.checkVarDefine(listeVariables, 'y2', -1)
        self.checkVarDefine(listeVariables, 'z1', '3')
        self.checkVarDefine(listeVariables, 'z2', '2')
        self.checkVarDefine(listeVariables, 'z3', '1')

    def test_construit2(self):
        tab2 = ['7', '8']
        listeVariables2: ListVariable = construit(tab2)
        self.assertEqual(5, len(listeVariables2.liste))
        self.checkVarDefine(listeVariables2, 'x1', -1)
        self.checkVarDefine(listeVariables2, 'x2', -1)
        self.checkVarDefine(listeVariables2, 'y1', -1)
        self.checkVarDefine(listeVariables2, 'z1', '8')
        self.checkVarDefine(listeVariables2, 'z2', '7')

    def getValeurs(self, listeMulti: list[Mult], nomVar: str) -> list[int]:
        listeVar: list[Variable] = getVariables(listeMulti, False)
        liste1: list[int] = [x.valeur for x in listeVar if x != None and x.nom.startswith(nomVar)]
        return liste1

    def check_calcul_resolution(self, nombre: str, res_ref: list[(list[int], list[int])]) -> None:
        res0: list[MultiplicationComplete] = []
        res0 = calcul_resolution(nombre, True)

        self.assertEqual(len(res_ref), len(res0))
        res_tuple: list[(list[int], list[int])] = []
        for res2 in res0:
            listx = self.getValeurs(res2.liste, 'x')
            listy = self.getValeurs(res2.liste, 'y')
            res_tuple.append((listx, listy))

        self.assertEqual(res_ref, res_tuple)

    def test_calcul_resolution21(self):
        nombre = '21'

        res_ref = [
            ([1, 2], [1]),
            ([3, 0], [7]),
            ([7, 0], [3])
        ]
        self.check_calcul_resolution(nombre, res_ref)

    def test_calcul_resolution115(self):
        nombre = '115'

        res_ref = [
            ([3, 2, 0], [5, 0]),
            ([5, 1, 1], [1, 0]),
            ([5, 0, 0], [3, 2])
        ]
        self.check_calcul_resolution(nombre, res_ref)

    def test_calcul_resolution28741(self):
        nombre = '28741'

        res_ref = [
            ([1, 0, 7, 0, 0], [1, 4, 0]),
            ([1, 4, 0, 0, 0], [1, 0, 7]),
            ([1, 4, 7, 8, 2], [1, 0, 0])
        ]
        self.check_calcul_resolution(nombre, res_ref)


if __name__ == '__main__':
    unittest.main()
