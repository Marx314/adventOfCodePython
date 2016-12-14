from unittest import TestCase
import unittest

from src.Year2016.Day14 import Day14


class Day14Test(TestCase):
    def setUp(self):
        self.day = Day14()

    def test_abc(self):
        starting_key = 'abc'
        result = self.day.one_time_pads(starting_key, 64, self.day.simple_md5)
        self.assertEqual(result[63], 22728)

    def test_puzzle(self):
        starting_key = 'ihaygndm'
        result = self.day.one_time_pads(starting_key, 64, self.day.simple_md5)
        self.assertEqual(result[63], 15035)

    def test_part2_hash_of_hash(self):
        starting_key = 'abc0'
        value = self.day.hash_2016(starting_key)
        self.assertEqual(value, 'a107ff634856bb300138cac6568c0f24')

    @unittest.skip("Take up to 2 minutes")
    def test_puzzle_part2(self):
        starting_key = 'ihaygndm'
        result = self.day.one_time_pads(starting_key, 64, self.day.hash_2016)
        self.assertEqual(result[63], 19968)
