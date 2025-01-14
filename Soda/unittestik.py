import unittest
from SodaType import Soda

class Test(unittest.Case):

    def test_supplement(self):
        ssoda=Soda()
        self.assertEqual(ssoda.show_my_drink(), "Обычная газировка")

    def test_supplement(self):
        ssoda=Soda(3)
        self.assertEqual(ssoda.show_my_drink(), "Обычная газировка")

if __name__ == '__main__':
    unittest.main()
    