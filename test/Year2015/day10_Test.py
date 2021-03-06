from unittest import TestCase

from src.Year2015.Day10 import Day10


class Day10Test(TestCase):
    def setUp(self):
        self.day = Day10()

    def test_one_one(self):
        self.assertEqual(len('11'), self.day.look_and_say_length('1'))
        self.assertEqual(len('21'), self.day.look_and_say_length('11'))
        self.assertEqual(len('1211'), self.day.look_and_say_length('21'))
        self.assertEqual(len('111221'), self.day.look_and_say_length('1211'))
        self.assertEqual(len('312211'), self.day.look_and_say_length('111221'))
        self.assertEqual(len('312211'), self.day.look_and_say_length('1', 5))

    def test_return_lookAndSayLength(self):
        self.assertEqual(904, self.day.look_and_say_length('1', 23))

    def test_puzzle(self):
        self.assertEqual(492982, self.day.look_and_say_length(self.puzzle(), repeat=40))
        self.assertEqual(6989950, self.day.look_and_say_length(self.puzzle(), repeat=50))

    def puzzle(self):
        return '1321131112'
