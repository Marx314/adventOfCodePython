from src.Year2016.Day5 import Day5
from unittest import TestCase


class Day5Test(TestCase):
    def setUp(self):
        self.day = Day5()

    def test_abc(self):
        door_id = 'abc'
        length = 2
        result = self.day.find_next(door_id, length)
        self.assertEqual(result, '18')

    def test_abc_three(self):
        door_id = 'abc'
        length = 3
        result = self.day.find_next(door_id, length)
        self.assertEqual(result, '18f')

    def test_abc_eight(self):
        door_id = 'abc'
        length = 8
        result = self.day.find_next(door_id, length)
        self.assertEqual(result, '18f47a30')

    def test_puzzle_eight(self):
        length = 8
        result = self.day.find_next(self.puzzle(), length)
        self.assertEqual(result, '4543c154')

    def test_abc_part2(self):
        door_id = 'abc'
        length = 2
        result = self.day.find_position(door_id, length)
        self.assertEqual(result, '05')

    def test_abc_eight_part3(self):
        door_id = 'abc'
        length = 8
        result = self.day.find_position(door_id, length)
        self.assertEqual(result, '05ace8e3')

    def test_puzzle_part2(self):
        length = 8
        result = self.day.find_position(self.puzzle(), length)
        self.assertEqual(result, '1050cbbd')

    def puzzle(self):
        return '''ojvtpuvg'''
