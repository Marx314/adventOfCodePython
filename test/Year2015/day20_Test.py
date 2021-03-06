from unittest import TestCase

from src.Year2015.Day20 import Day20, houses_of_cards, houses_of_cards_sum


class Day20Test(TestCase):
    def setUp(self):
        self.day = Day20()

    def test_nine_house_nine_elf(self):
        houses = [10, 30, 40, 70, 60, 120, 80, 150, 130]
        self.assertEqual(houses, houses_of_cards(9))

    def test_ninty_nine_house_nine_elf(self):
        houses = [10, 30, 40, 70, 60, 120, 80, 150, 130]
        self.assertEqual(houses, houses_of_cards(9))

    def test_index_of_sum_nine_house_nine_elf(self):
        self.assertEqual(8, houses_of_cards_sum(150))

    def test_puzzle_house(self):
        self.assertEqual(665280, houses_of_cards_sum(self.puzzle(), starting_at=665000))

    def test_puzzle_house_fifty(self):
        self.assertEqual(705600, self.day.houses_of_cards_sum_fifty(self.puzzle(), starting_at=705000))

    def puzzle(self):
        return 29000000