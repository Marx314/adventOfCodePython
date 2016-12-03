from src.Year2016.Day1 import Day1
from unittest import TestCase


class Day1Test(TestCase):
    def setUp(self):
        self.day = Day1()

    def tearDown(self):
        pass

    def test_case1(self):
        result = self.day.calc('R2, L3')
        self.assertEqual(result['north'], 3)
        self.assertEqual(result['east'], 2)
        self.assertEqual(result['distance'], 5)

    def test_case2(self):
        result = self.day.calc('R2, R2, R2')
        self.assertEqual(result['south'], 2)
        self.assertEqual(result['distance'], 2)

    def test_case3(self):
        result = self.day.calc('R5, L5, R5, R3')
        self.assertEqual(result['distance'], 12)

    def test_casePuzzle(self):
        result = self.day.calc(self.puzzle())
        self.assertEqual(result, {'west': 193, 'east': 336, 'north': 327, 'south': 191, 'distance': 279})

    def test_visitTwice(self):
        result = self.day.distance_from_first_crossing_path('R8, R4, R4, R8')
        self.assertEqual(result, 4)

    def test_visitTwicePuzzle(self):
        result = self.day.distance_from_first_crossing_path(self.puzzle())
        self.assertEqual(result, 5 + 158)

    def puzzle(self):
        return 'L4, L1, R4, R1, R1, L3, R5, L5, L2, L3, R2, R1, L4, R5, R4, L2, R1, R3, L5, R1, L3, L2, R5, L4, L5, R1, R2, L1, R5, L3, R2, R2, L1, R5, R2, L1, L1, R2, L1, R1, L2, L2, R4, R3, R2, L3, L188, L3, R2, R54, R1, R1, L2, L4, L3, L2, R3, L1, L1, R3, R5, L1, R5, L1, L1, R2, R4, R4, L5, L4, L1, R2, R4, R5, L2, L3, R5, L5, R1, R5, L2, R4, L2, L1, R4, R3, R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4, R2, R5, L2, L5, R4, L3, L2, R1, R1, L5, L4, R1, L5, L1, L5, L1, L4, L3, L5, R4, R5, R2, L5, R5, R5, R4, R2, L1, L2, R3, R5, R5, R5, L2, L1, R4, R3, R1, L4, L2, L3, R2, L3, L5, L2, L2, L1, L2, R5, L2, L2, L3, L1, R1, L4, R2, L4, R3, R5, R3, R4, R1, R5, L3, L5, L5, L3, L2, L1, R3, L4, R3, R2, L1, R3, R1, L2, R4, L3, L3, L3, L1, L2'
