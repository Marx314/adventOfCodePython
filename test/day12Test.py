from unittest import TestCase
from src.Day11 import Day11


class Day11Test(TestCase):
    def setUp(self):
        self.day = Day11()

    def tearDown(self):
        pass

    def test_one_one(self):
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
        self.assertNotEqual('hxcaabcc', self.day.generate('hxbxwxba')) # because I've forget to +1
        self.assertEqual('hxbxxyzz', self.day.generate('hxbxwxba'))
        self.assertEqual('hxcaabcc', self.day.generate('hxbxxyzz'))


