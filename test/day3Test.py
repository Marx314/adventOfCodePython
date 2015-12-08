from unittest import TestCase
from src.Day3 import Day3


class Day3Test(TestCase):
    def setUp(self):
        self.day = Day3()

    def tearDown(self):
        pass

    def test_two_houses(self):
        data = '>'
        self.assertEqual(2, self.day.calc(data))

    def test_five_present_four_house(self):
        data = '^>v<'
        self.assertEqual(4, self.day.calc(data))

    def test_two_houses_eggnog_effect(self):
        data = '^v^v^v^v^v'
        self.assertEqual(2, self.day.calc(data))

    def test_two_santa_simple(self):
        data = '^v'
        self.assertEqual(3, self.day.two_santa(data))

    def test_two_santa_three_house(self):
        data = '^>v<'
        self.assertEqual(3, self.day.two_santa(data))

    def test_two_santa_11_house(self):
        data = '^v^v^v^v^v'
        self.assertEqual(11, self.day.two_santa(data))

