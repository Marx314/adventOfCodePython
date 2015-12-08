from unittest import TestCase
from src.Day4 import Day4


class Day4Test(TestCase):
    def setUp(self):
        self.day = Day4()

    def tearDown(self):
        pass

    def test_keys_simple(self):
        key = 'abcdef'
        self.assertEqual('609043', self.day.calc(key))
        key = 'pqrstuv'
        self.assertEqual('1048970', self.day.calc(key))


