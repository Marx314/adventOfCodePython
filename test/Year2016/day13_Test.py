from unittest import TestCase

from src.Year2016.Day13 import WALL, EMPTY, Day13


class Day13Test(TestCase):
    def setUp(self):
        self.day = Day13()

    def test_base(self):
        puzzle = self.day.build_puzzle(10, 10)

        self.assertEqual(EMPTY, puzzle[4 * 10 + 7])
        self.assertEqual(WALL, puzzle[3 * 10 + 7])

        result = self.day.shortest_path_cost(puzzle, (7, 4))
        self.assertEqual(result, 11)

    def test_puzzle(self):
        puzzle = self.day.build_puzzle(50, 1352)

        self.assertEqual(EMPTY, puzzle[39 * 50 + 31])

        path_length, different_location = self.day.path_length_and_location_within_50_step(puzzle, (31, 39))
        self.assertEqual(path_length, 90)
        self.assertEqual(different_location, 135)
