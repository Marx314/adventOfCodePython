from unittest import TestCase
import unittest

from src.Year2016.Day16 import Day16


class Day16Test(TestCase):
    def setUp(self):
        self.day = Day16()

    def test_basic(self):
        self.assertEqual(self.day.generate_data('1'), '100')
        self.assertEqual(self.day.generate_data('0'), '001')
        self.assertEqual(self.day.generate_data('11111'), '11111000000')
        self.assertEqual(self.day.generate_data('111100001010'), '1111000010100101011110000')

    def test_all(self):
        result = self.day.generate_data_until('10000', 20)
        self.assertEqual(result, '10000011110010000111')
        result = self.day.checksum(result)
        self.assertEqual(result, '01100')

    def test_checksum(self):
        result = self.day.checksum('110010110100')
        self.assertEqual(result, '100')

    def test_puzzle(self):
        result = self.day.generate_data_until(self.puzzle(), 272)
        result = self.day.checksum(result)
        self.assertEqual(result, '10100101010101101')

    @unittest.skip('ain\'t got time for that')
    def test_puzzle_part2(self):
        result = self.day.generate_data_until(self.puzzle(), 35651584)
        result = self.day.checksum(result)
        self.assertEqual(result, '01100001101101001')

    def puzzle(self):
        return '''11101000110010100'''
