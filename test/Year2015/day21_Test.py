from unittest import TestCase

from src.Year2015.Day21 import Day21


class Day21Test(TestCase):
    def setUp(self):
        self.day = Day21()

    def test_simple_battle(self):
        you = {'hp': 8, 'damage': 5, 'armor': 5}
        boss = {'hp': 12, 'damage': 7, 'armor': 2}
        self.assertTrue(self.day.doyousurviveagainstboss(you, boss))

    def test_still_1_damage_against_strong_armor(self):
        you = {'hp': 8, 'damage': 5, 'armor': 5}
        boss = {'hp': 2, 'damage': 5, 'armor': 500}
        self.assertTrue(self.day.doyousurviveagainstboss(you, boss))

    # TODO(marx314) 21!
    # def test_minimal_cost(self):
    #    you = {'hp': 8, 'damage': 5, 'armor': 5}
    #    boss = {'hp': 12, 'damage': 7, 'armor': 2}
    #    self.assertEqual(8, self.day.minimal_cost(you, boss))

    def boss(self):
        return {'hp': 104, 'damage': 8, 'armor': 1}
