from unittest import TestCase

from src.Year2015.Day4 import Day4


class Day4Test(TestCase):
    def setUp(self):
        self.day = Day4()

    def test_keys_simple(self):
        self.assertEqual('609043', self.day.calc('abcdef'))
        self.assertEqual('1048970', self.day.calc('pqrstuv'))

    def test_puzzle(self):
        self.assertEqual('282749', self.day.calc(self.puzzle()))
        self.assertEqual('9962624', self.day.calc6(self.puzzle()))

    def puzzle(self):
        return 'yzbqklnj'
