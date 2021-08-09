import unittest


class PruebaDeStandards(unittest.TestCase):

    def test_suma(self):
        a = 2 + 2
        b = 3 + 1
        self.assertEqual(a, b)

    def test_otra_suma(self):
        a = 5 + 1
        b = 8 + 20
        self.assertNotEqual(a, b)

    def test_algo_es_verdadero(self):
        a = 5+4
        b = 3+6
        self.assertTrue(a == b)

    def test_algo_mas_es_verdadero(self):
        self.assertTrue(3+3 == 4+2)

    def test_algo_es_falso(self):
        self.assertFalse(2+1 == 3+5)

    def test_otro_falso(self):
        self.assertFalse(3+5 == 2+4, 'Esto deberia ser falso')

    def test_algo_es_mayor(self):
        a = 5
        b = 3
        self.assertTrue(a > b)

    def test_otra_cosa_es_mayor(self):
        a = 5
        b = 2
        self.assertGreater(a, b, 'El primero debe ser mas grande que el segundo')

    def test_algo_es_mayor_o_igual(self):
        a = 5
        b = 4
        self.assertGreaterEqual(a, b)

    def test_algo_es_menor(self):
        a = 5
        b = 8
        self.assertLess(a, b)

    def test_algo_es_menor_o_igual(self):
        a = 4
        b = 4
        self.assertLessEqual(a, b)

    def test_comparar_listas(self):
        a = [1, 2, 'Fruta']
        b = [1, 2, 'Fruta']
        self.assertListEqual(a, b)

    def test_comparar_tuplas(self):
        a = (1, 2, 3)
        b = (1, 2, 3)
        self.assertTupleEqual(a, b)

    def test_comparar_diccionarios(self):
        a = {'id':1, 'Nombre':'Nelson', 'Apellido':'Perez'}
        b = {'id':1, 'Nombre':'Nelson', 'Apellido':'Perez'}
        self.assertDictEqual(a, b)
        


if __name__ == '__main__':
    unittest.main()

