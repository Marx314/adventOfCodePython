from unittest import TestCase

from src.Year2015.Day25 import Day25


class Day25Test(TestCase):
    def setUp(self):
        self.day = Day25()

    def simple_puzzle(self):
        return '''20151125'''

    def test_generate_1row_2col_from_first(self):
        self.assertEqual(18749137, self.day.generate(row=1, col=2, start=self.simple_puzzle()))

    def test_generate_2row_2col_from_first(self):
        self.assertEqual(21629792, self.day.generate(row=2, col=2, start=self.simple_puzzle()))

    def test_generate_3row_3col_from_first(self):
        self.assertEqual(1601130, self.day.generate(row=3, col=3, start=self.simple_puzzle()))

    def test_generate_puzzle_step1(self):
        self.assertEqual(8997277, self.day.generate(row=3010, col=3019, start=self.simple_puzzle()))

    # TODO(marx314) 25 part 2 when others are done!
    def puzzle(self):
        return ''''''
