from unittest import TestCase
from src.Day20 import Day20


class Day20Test(TestCase):
    def setUp(self):
        self.day = Day20()

    def tearDown(self):
        pass

    def test_nine_house_nine_elf(self):
        houses = [10, 30, 40, 70, 60, 120, 80, 150, 130]
        self.assertEqual(houses, self.day.houses_of_cards(9))

    def test_ninty_nine_house_nine_elf(self):
        houses = [10, 30, 40, 70, 60, 120, 80, 150, 130]
        self.assertEqual(houses, self.day.houses_of_cards(9))

    def test_index_of_sum_nine_house_nine_elf(self):
        self.assertEqual(8, self.day.houses_of_cards_sum(150))

    def test_puzzle_house(self):
        self.assertEqual(665280, self.day.houses_of_cards_sum(self.puzzle()))

    def test_puzzle_house_fifty(self):
        self.assertEqual(705600, self.day.houses_of_cards_sum_fifty(self.puzzle()))

    def puzzle(self):
        return 29000000

