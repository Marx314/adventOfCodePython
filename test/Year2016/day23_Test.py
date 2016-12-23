from unittest import TestCase
import unittest

from src.Year2016.Day23 import Day23


class Day23Test(TestCase):
    def setUp(self):
        self.day = Day23()

    def test_base(self):
        register = {'a': 0}
        self.assertEqual(self.day.program(self.base(), register=register)['a'], 3)

    def test_puzzle(self):
        register = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
        self.assertEqual(self.day.program(self.puzzle(), register=register)['a'], 10661)

    @unittest.skip('TLDR')
    def test_puzzle_part2(self):
        register = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
        self.assertEqual(self.day.program(self.puzzle(), register=register)['a'], 479007221)

    def base(self):
        return '''cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a'''

    def puzzle(self):
        return '''cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -16 c
jnz 1 c
cpy 77 c
jnz 73 d
inc a
inc d
jnz d -2
inc c
jnz c -5'''
