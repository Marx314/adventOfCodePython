from unittest import TestCase

from src.Year2015.Day22 import Boss, You, Day22


class Day22Test(TestCase):
    def setUp(self):
        self.day = Day22()

    def test_puzzle(self):
        y = You(50, 500)
        b = Boss(51, 9)
        mana_cost = self.day.find_best_fight_config(y, b)
        self.assertEqual(mana_cost, 900)

    def test_puzzle_part2(self):
        y = You(50, 500)
        b = Boss(51, 9)
        mana_cost = self.day.find_best_fight_config_hard(y, b)
        self.assertEqual(mana_cost, 1216)
