from unittest import TestCase

from src.Year2016.Day13 import WALL, EMPTY, Day13


class Day13Test(TestCase):
    def setUp(self):
        self.day = Day13()

    def test_base(self):
        puzzle = self.day.build_puzzle(size=10, favorite_number=10)

        self.assertEqual(EMPTY, puzzle[4 * 10 + 7])
        self.assertEqual(WALL, puzzle[3 * 10 + 7])
        cost_so_far, came_from, current, position = self.day.a_star_search(puzzle, (7, 4), 50)
        self.assertEqual(cost_so_far[current], 11)

    def test_puzzle(self):
        puzzle = self.day.build_puzzle(size=50, favorite_number=1352)

        self.assertEqual(EMPTY, puzzle[39 * 50 + 31])
        cost_so_far, came_from, current, positions = self.day.a_star_search(puzzle, (31, 39), 50)

        self.assertEqual(cost_so_far[current], 90)
        self.assertEqual(positions, 135)
