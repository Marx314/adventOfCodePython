from unittest import TestCase
import unittest

from src.Year2016.Day18 import Day18


class Day18Test(TestCase):
    def setUp(self):
        self.day = Day18()

    def test_simple_row(self):
        row = '..^^.'
        result = self.day.get_next_row(row)
        self.assertEqual(result, '.^^^^')
        result = self.day.get_next_row(result)
        self.assertEqual(result, '^^..^')

    def test_ten_row_count(self):
        row = '.^^.^.^^^^'
        count = self.day.calculate_safe_tiles(row)
        self.assertEqual(count, 38)

    def test_puzzle_part1(self):
        count = self.day.calculate_safe_tiles(self.puzzle(), 40)
        self.assertEqual(count, 2005)

    @unittest.skip('30 seconds, make test not sleep!')
    def test_puzzle_part2(self):
        count = self.day.calculate_safe_tiles(self.puzzle(), 400000)
        self.assertEqual(count, 20008491)

    def puzzle(self):
        return '''.^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^'''
