from unittest import TestCase
from src.Day13 import Day13
from src.Day14 import Day14
from src.Day15 import Day15


class Day15Test(TestCase):
    def setUp(self):
        self.day = Day15()

    def tearDown(self):
        pass

    def test_simple_best_cookies(self):
        self.assertEqual(62842880, self.day.cookies(self.simple_puzzle()))

    def test_simple_best_cookie_with_only_500cal(self):
        self.assertEqual(57600000, self.day.cookies(self.simple_puzzle(), only500cal=True))

    def simple_puzzle(self):
        return '''Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'''

    def test_puzzle_best_cookie(self):
        self.assertEqual(18965440, self.day.cookies(self.puzzle()))

    def test_puzzle_best_cookie_with_only_500cal(self):
        self.assertEqual(15862900, self.day.cookies(self.puzzle(), only500cal=True))

    def puzzle(self):
        return '''Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1'''