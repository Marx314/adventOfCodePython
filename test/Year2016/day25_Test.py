from unittest import TestCase

import copy
from src.Year2016.Day25 import NoPatternFor, Found, Day25


class Day25Test(TestCase):
    def setUp(self):
        self.day = Day25()

    def test_puzzle(self):
        register = {'a': 158, 'b': 0, 'c': 0, 'd': 0}
        while True:
            try:
                self.day.program(self.puzzle(), register=copy.deepcopy(register))
            except NoPatternFor:
                register['a'] += 1
            except Found:
                break
        self.assertEqual(register['a'], 158)

    def puzzle(self):
        return '''cpy a d
cpy 4 c
cpy 643 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy d a
jnz 0 0
cpy a b
cpy 0 a
cpy 2 c
jnz b 2
jnz 1 6
dec b
dec c
jnz c -4
inc a
jnz 1 -7
cpy 2 b
jnz c 2
jnz 1 4
dec b
dec c
jnz 1 -4
jnz 0 0
out b
jnz a -19
jnz 1 -21'''
