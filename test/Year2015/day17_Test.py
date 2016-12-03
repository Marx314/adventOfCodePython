from unittest import TestCase

from src.Year2015.Day17 import Day17


class Day17Test(TestCase):
    def setUp(self):
        self.day = Day17()

    def test_simple_container(self):
        self.assertEqual(4, len(self.day.generate_combinaison(self.simple_puzzle())))

    def test_simple_container_step2(self):
        self.assertEqual(3, self.day.how_many_minimum(self.simple_puzzle()))

    def simple_puzzle(self):
        return '''20
15
10
5
5'''

    def test_puzzle_container(self):
        self.assertEqual(4372, len(self.day.generate_combinaison(self.puzzle(), liter=150)))

    def test_puzzle_container_step2(self):
        self.assertEqual(4, self.day.how_many_minimum(self.puzzle(), liter=150))

    def puzzle(self):
        return '''11
30
47
31
32
36
3
1
5
3
32
36
15
11
46
26
28
1
19
3'''
