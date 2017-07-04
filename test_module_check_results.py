import unittest
from pokerstrat import main


class TestEachAnswer(unittest.TestCase):

    def test_straight_flush(self):
        self.assertEqual(main(data=['TH JH QC QD QS QH KH AH 2S 6S'], silent=True),
                         [[['TH', 'JH', 'QC', 'QD', 'QS'], ['QH', 'KH', 'AH', '2S', '6S'], 'straight-flush']])

    def test_four(self):
        self.assertEqual(main(data=['2H 2S 3H 3S 3C 2D 3D 6C 9C TH'], silent=True),
                         [[['2H', '2S', '3H', '3S', '3C'], ['2D', '3D', '6C', '9C', 'TH'], 'four-of-a-kind']])

    def test_full_house(self):
        self.assertEqual(main(data=['2H 2S 3H 3S 3C 2D 9C 3D 6C TH'], silent=True),
                         [[['2H', '2S', '3H', '3S', '3C'], ['2D', '9C', '3D', '6C', 'TH'], 'full-house']])

    def test_flush(self):
        self.assertEqual(main(data=['2H AD 5H AC 7H AH 6H 9H 4H 3C'], silent=True),
                         [[['2H', 'AD', '5H', 'AC', '7H'], ['AH', '6H', '9H', '4H', '3C'], 'flush']])

    def test_straight(self):
        self.assertEqual(main(data=['AC 2D 9C 3S KD 5S 4D KS AS 4C'], silent=True),
                         [[['AC', '2D', '9C', '3S', 'KD'], ['5S', '4D', 'KS', 'AS', '4C'], 'straight']])

    def test_triple(self):
        self.assertEqual(main(data=['KS AH 2H 3C 4H KC 2C TC 2D AS'], silent=True),
                         [[['KS', 'AH', '2H', '3C', '4H'], ['KC', '2C', 'TC', '2D', 'AS'], 'three-of-a-kind']])

    def test_double(self):
        self.assertEqual(main(data=['AH 2C 9S AD 3C QH KS JS JD KD'], silent=True),
                         [[['AH', '2C', '9S', 'AD', '3C'], ['QH', 'KS', 'JS', 'JD', 'KD'], 'two-pair']])

    def test_double(self):
        self.assertEqual(main(data=['6C 9C 8C 2D 7C 2H TC 4C 9S AH'], silent=True),
                         [[['6C', '9C', '8C', '2D', '7C'], ['2H', 'TC', '4C', '9S', 'AH'], 'one-pair']])

    def test_double(self):
        self.assertEqual(main(data=['3D 5S 2H QD TD 6S KH 9H AD QH'], silent=True),
                         [[['3D', '5S', '2H', 'QD', 'TD'], ['6S', 'KH', '9H', 'AD', 'QH'],'highest card']])


if __name__ == '__main__':
    unittest.main()
