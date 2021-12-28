import unittest

from premier import isprime, listePrime


class PremierTestCase(unittest.TestCase):

    def test_isprime(self):
        self.assertTrue(isprime(2))
        self.assertTrue(isprime(3))
        self.assertFalse(isprime(4))
        self.assertTrue(isprime(5))
        self.assertFalse(isprime(6))
        self.assertTrue(isprime(7))
        self.assertFalse(isprime(8))
        self.assertFalse(isprime(9))
        self.assertFalse(isprime(10))
        self.assertTrue(isprime(11))
        self.assertFalse(isprime(12))
        self.assertTrue(isprime(13))
        self.assertFalse(isprime(14))

    listResultat: list[int] = []

    def fonction(self, x: int):
        self.listResultat.append(x)

    def test_listePrime(self):
        self.listResultat = []
        listePrime(20, self.fonction)
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19], self.listResultat)



if __name__ == '__main__':
    unittest.main()
