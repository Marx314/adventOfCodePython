from unittest import TestCase
from src.Day9 import Day9


class Day9Test(TestCase):
    def setUp(self):
        self.day = Day9()

    def tearDown(self):
        pass

    def test_empty_string(self):
        instructions = [
            'London to Dublin = 464',
            'London to Belfast = 518',
            'Dublin to Belfast = 141',
        ]
        self.assertEqual(605, self.day.calc(instructions))


