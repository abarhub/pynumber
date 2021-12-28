import unittest

from test1 import ListVariable, construit


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


if __name__ == '__main__':
    unittest.main()
