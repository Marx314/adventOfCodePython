from unittest import TestCase
import unittest

from src.Year2016.Day15 import Day15


class Day15Test(TestCase):
    def setUp(self):
        self.day = Day15()

    def test_basic(self):
        instructions = '''Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.'''
        result = self.day.get_perfect_timing(instructions)
        self.assertEqual(result, 5)

    def test_puzzle_part1(self):
        result = self.day.get_perfect_timing(self.puzzle())
        self.assertEqual(result, 400589)

    @unittest.skip('ain\'t got time for that')
    def test_puzzle_part2(self):
        result = self.day.get_perfect_timing(self.puzzle_part2())
        self.assertEqual(result, 3045959)

    def puzzle(self):
        return '''Disc #1 has 17 positions; at time=0, it is at position 15.
Disc #2 has 3 positions; at time=0, it is at position 2.
Disc #3 has 19 positions; at time=0, it is at position 4.
Disc #4 has 13 positions; at time=0, it is at position 2.
Disc #5 has 7 positions; at time=0, it is at position 2.
Disc #6 has 5 positions; at time=0, it is at position 0.'''

    def puzzle_part2(self):
        return '''{}
Disc #7 has 11 positions; at time=0, it is at position 0.'''.format(self.puzzle())
