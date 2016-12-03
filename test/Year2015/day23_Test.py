from unittest import TestCase

from src.Year2015.Day23 import Day23


class Day20Test(TestCase):
    def setUp(self):
        self.day = Day23({'a': 0, 'b': 0})

    def test_42(self):
        self.assertEqual(2, self.day.program(self.simple_puzzle())['a'])

    def simple_puzzle(self):
        return '''inc a
jio a, +2
tpl a
inc a'''

    def test_puzzle(self):
        self.day = Day23({'a': 0, 'b': 0})
        self.assertEqual(170, self.day.program(self.puzzle())['b'])

    def test_puzzle_step_two(self):
        self.day = Day23({'a': 1, 'b': 0})
        self.assertEqual(247, self.day.program(self.puzzle())['b'])

    def puzzle(self):
        return '''jio a, +16
inc a
inc a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +23
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
inc a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7'''
