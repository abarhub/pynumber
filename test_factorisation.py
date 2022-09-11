from unittest import TestCase

from factorisation import Resolution, ListValue, MultiplicationComplete


class Test(TestCase):

    # def test_main(self):
    #     self.fail()

    def test_main21(self):
        n = '21'
        resolution = Resolution()
        listValue = ListValue()
        res = resolution.calcul_resolution(n, False, listValue.listValue)
        self.assertEqual(3, len(res))
        self.assertEqual("x1", res[0].getByOrder(0)[0].x.nom)
        self.assertEqual(1, res[0].getByOrder(0)[0].x.valeur)
        self.assertEqual("y1", res[0].getByOrder(0)[0].y.nom)
        self.assertEqual(1, res[0].getByOrder(0)[0].y.valeur)

    def test_main21_bis(self):
        n = '21'
        resolution = Resolution()
        listValue = ListValue()
        res = resolution.calcul_resolution(n, False, listValue.listValue)
        tmp = self.getListValues(res)
        print("tmp=", tmp)

        for n in tmp:
            self.assertEqual(21, n['x'] * n['y'])

        self.assertEqual(3, len(tmp))
        self.assertIn({'x': 3, 'y': 7}, tmp)
        self.assertIn({'x': 7, 'y': 3}, tmp)
        self.assertIn({'x': 21, 'y': 1}, tmp)

    def test_main115(self):
        n = '115'
        resolution = Resolution()
        listValue = ListValue()
        res = resolution.calcul_resolution(n, False, listValue.listValue)
        tmp = self.getListValues(res)
        print("tmp=", tmp)

        for n in tmp:
            self.assertEqual(115, n['x'] * n['y'])

        self.assertEqual(3, len(tmp))
        self.assertIn({'x': 23, 'y': 5}, tmp)
        self.assertIn({'x': 5, 'y': 23}, tmp)
        self.assertIn({'x': 115, 'y': 1}, tmp)

    def test_main28741(self):
        n = '28741'
        resolution = Resolution()
        listValue = ListValue()
        res = resolution.calcul_resolution(n, False, listValue.listValue)
        tmp = self.getListValues(res)
        print("tmp=", tmp)

        for n in tmp:
            self.assertEqual(28741, n['x'] * n['y'])

        self.assertEqual(3, len(tmp))
        self.assertIn({'x': 701, 'y': 41}, tmp)
        self.assertIn({'x': 41, 'y': 701}, tmp)
        self.assertIn({'x': 28741, 'y': 1}, tmp)

    def test_main99400891(self):
        n = '99400891'
        resolution = Resolution()
        listValue = ListValue()
        res = resolution.calcul_resolution(n, False, listValue.listValue)
        tmp = self.getListValues(res)
        print("tmp=", tmp)

        for n in tmp:
            self.assertEqual(99400891, n['x'] * n['y'])

        self.assertEqual(3, len(tmp))
        self.assertIn({'x': 9973, 'y': 9967}, tmp)
        self.assertIn({'x': 9967, 'y': 9973}, tmp)
        self.assertIn({'x': 99400891, 'y': 1}, tmp)

    def getListValues(selft, listValues: list[MultiplicationComplete]):
        res: list[(int, int)] = []
        for m in listValues:
            x = 0
            no = 0
            for n in m.getX():
                x = n * (10 ** no) + x
                no += 1
            y = 0
            no = 0
            for n in m.getY():
                y = n * (10 ** no) + y
                no += 1
            res.append({'x': x, 'y': y})
        return res
