from unittest import TestCase

from src.Year2015.Day11 import Day11


class Day11Test(TestCase):
    def setUp(self):
        self.day = Day11()

    def test_requirement(self):
        self.assertEqual(True, self.day.is_valid('ghjaabcc'))

        self.assertEqual(True, self.day.first_requirement('hijklmmn'))
        self.assertEqual(False, self.day.second_requirement('hijklmmn'))
        self.assertEqual(False, self.day.third_requirement('hijklmmn'))

        self.assertEqual(False, self.day.first_requirement('abbceffg'))
        self.assertEqual(True, self.day.second_requirement('abbceffg'))
        self.assertEqual(True, self.day.third_requirement('abbceffg'))

        self.assertEqual(False, self.day.first_requirement('abbcegjk'))
        self.assertEqual(True, self.day.second_requirement('abbcegjk'))
        self.assertEqual(False, self.day.third_requirement('abbcegjk'))

    def test_generation(self):
        self.assertEqual('ghjaabcc', self.day.generate('ghijklmn'))
        self.assertEqual('abcdffaa', self.day.generate('abcdefgh'))

    def test_puzzle(self):
        self.assertEqual('hxbxxyzz', self.day.generate('hxbxwxba'))
        self.assertEqual('hxcaabcc', self.day.generate('hxbxxyzz'))
