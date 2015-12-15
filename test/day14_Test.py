from unittest import TestCase
from src.Day14 import Day14


class Day14Test(TestCase):
    def setUp(self):
        self.day = Day14()

    def tearDown(self):
        pass

    def test_comet_vs_dancer(self):
        self.assertEqual(1120, self.day.max_distance(self.simple_puzzle(), time=1000))

    def test_comet_vs_dancer_point(self):
        self.assertEqual(689, self.day.max_point(self.simple_puzzle(), time=1000))

    def simple_puzzle(self):
        return '''Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'''

    def test_om_my_deer(self):
        self.assertEqual(2696, self.day.max_distance(self.puzzle(), time=2503))

    def test_om_my_deer_point(self):
        self.assertEqual(1084, self.day.max_point(self.puzzle(), time=2503))

    def puzzle(self):
        return '''Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.
Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.
Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.
Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.
Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.
Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds.'''