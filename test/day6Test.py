from unittest import TestCase
from src.Day6 import Day6


class Day6Test(TestCase):
    def setUp(self):
        self.day = Day6()

    def tearDown(self):
        pass

    def test_one_brightness(self):
        instruction = ['turn on 0,0 through 0,0']
        self.assertEqual(1, self.day.calc_bright(instruction))

    def test_all_brightness(self):
        instruction = ['toggle 0,0 through 999,999']
        self.assertEqual(2000000, self.day.calc_bright(instruction))

    def test_all_light(self):
        instruction = ['turn on 0,0 through 999,999']
        self.assertEqual(1000000, self.day.calc(instruction))

    def test_toggle_first_line(self):
        instruction = ['toggle 0,0 through 999,0']
        self.assertEqual(1000, self.day.calc(instruction))

    def test_all_light_minus_four_in_middle(self):
        instruction = ['turn on 0,0 through 999,999', 'turn off 499,499 through 500,500']
        self.assertEqual(1000000-4, self.day.calc(instruction))
