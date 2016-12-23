from unittest import TestCase
import unittest

from src.Year2016.Day12 import Day12


class Day12Test(TestCase):
    def setUp(self):
        self.day = Day12()

    def test_base(self):
        register = {'a': 0, 'b': 0}
        self.assertEqual(self.day.program(self.base(), register=register)['a'], 42)

    def base(self):
        return '''cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a'''

    def test_puzzle(self):
        register = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        self.assertEqual(self.day.program(self.puzzle(), register=register)['a'], 317993)

    @unittest.skip('wait a minute')
    def test_puzzle_part2(self):
        register = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
        self.assertEqual(self.day.program(self.puzzle(), register=register)['a'], 9227647)

    def puzzle(self):
        return '''cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 13 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5'''
