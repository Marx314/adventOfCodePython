from unittest import TestCase

from src.Year2015.Day21 import Day21, win_against_boss, lose_against_boss, Build


class Day21Test(TestCase):
    def setUp(self):
        self.day = Day21()

    def test_simple_battle(self):
        you = Build({'hp': 8, 'damage': 5, 'armor': 5})
        boss = {'hp': 12, 'damage': 7, 'armor': 2}
        self.assertTrue(win_against_boss(you, boss))

    def test_still_1_damage_against_strong_armor(self):
        you = Build({'hp': 8, 'damage': 5, 'armor': 5})
        boss = {'hp': 2, 'damage': 5, 'armor': 500}
        self.assertTrue(win_against_boss(you, boss))

    def test_win_cheap(self):
        you = {'hp': 100, 'damage': 0, 'armor': 0}
        builds = self.day.iterate_build(you, self.puzzle())
        self.assertEqual(builds[0].cost, 78)

    def test_lose_expensive(self):
        you = {'hp': 100, 'damage': 0, 'armor': 0}
        builds = self.day.iterate_build(you, self.puzzle(), lose_against_boss)
        self.assertEqual(builds[-1].cost, 148)

    def puzzle(self):
        return {'hp': 104, 'damage': 8, 'armor': 1}
